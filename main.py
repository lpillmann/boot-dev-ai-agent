import os
import sys
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function

from pprint import pprint


load_dotenv()

MAX_ITERATIONS = 20


system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
Represent the root directory as "."
"""

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)


def main(user_prompt: str, is_verbose: bool = False):
    """Main function to generate content using Google Gemini AI."""
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # outer loop for more than one round of user prompt
    while True:
        iterations = 0
        while True:
            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=messages,
                    config=types.GenerateContentConfig(
                        tools=[available_functions], system_instruction=system_prompt
                    ),
                )
                if response.candidates:
                    for candidate in response.candidates:
                        messages.append(candidate.content)

                if response.function_calls:
                    for function_call_part in response.function_calls:
                        print(
                            f"Calling function: {function_call_part.name}({function_call_part.args})"
                        )

                        try:
                            function_response_content = call_function(
                                function_call_part, is_verbose
                            )
                            messages.append(function_response_content)

                        except Exception as e:
                            raise f"Error: fatal - no result from function call received: {repr(e)}"
                    continue

                if response.text:
                    print(f"\n=== Response ===\n{response.text}")
                    if is_verbose:
                        print(f"User prompt: {user_prompt}")
                        print(
                            f"Prompt tokens: {response.usage_metadata.prompt_token_count}"
                        )
                        print(
                            f"Response tokens: {response.usage_metadata.candidates_token_count}"
                        )
                    break

                else:
                    print("Stopping. Model returned empty response.")

                if is_verbose:
                    print(f">> Iterations count: {iterations}")

            except Exception as e:
                raise e

            iterations += 1
            time.sleep(1)
            if iterations >= MAX_ITERATIONS:
                print("Maximum iterations reached. Stopping.")
                break

        next_user_prompt = input("\n> ")
        messages.append(
            types.Content(role="user", parts=[types.Part(text=next_user_prompt)])
        )


if __name__ == "__main__":
    is_verbose = "--verbose" in sys.argv
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        raise SystemExit(1)

    user_prompt = sys.argv[1]
    try:
        main(user_prompt, is_verbose)
    except KeyboardInterrupt:
        print("Exiting")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
