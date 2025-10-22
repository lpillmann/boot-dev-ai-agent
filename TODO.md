where I stopped
- trying to figure out how to properly build the loop
  - it is able to run iterations of more complex tasks e.g.
    - uv run main.py "explain how the calculator renders the result to the console."
  - however, it gets lost for simple requests that worked before
    - uv run main.py "what are the files in the root folder?"
    - the last break is a bit weird
      --> read again the instructions and review the code
- CURRENTLY MIGHT BE BROKEN DUE TO CHANGES IN HOW FUNCTION RESPONSE CONTENT IS HANDLEDED
  - the returned object of call_function is already a content, which can be passed as a message
