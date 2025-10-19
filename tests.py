import unittest

# from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# from functions.config import MAX_CHARS_FROM_FILE, MAX_CHARS_ERROR_MSG_TEMPLATE
# from functions.write_file import write_file
from functions.run_python_file import run_python_file


class TestStringMethods(unittest.TestCase):
    # def test_root(self):
    #     output = get_files_info("calculator", ".")
    #     print(output)
    #     num_lines = len(output.split("\n"))
    #     expected_items = 3
    #     self.assertEqual(True, "pkg" in output)
    #     self.assertEqual(True, "main.py" in output)
    #     self.assertEqual(True, "tests.py" in output)
    #     self.assertEqual(True, num_lines == expected_items + 1)

    # def test_pkg(self):
    #     output = get_files_info("calculator", "pkg")
    #     print(output)
    #     num_lines = len(output.split("\n"))
    #     expected_items = 3
    #     self.assertEqual(True, "__pycache__" in output)
    #     self.assertEqual(True, "calculator.py" in output)
    #     self.assertEqual(True, "render.py" in output)
    #     self.assertEqual(True, num_lines == expected_items + 1)

    # def test_bin(self):
    #     output = get_files_info("calculator", "/bin")
    #     print(output)
    #     expected = (
    #         'Error: Cannot list "/bin" as it is outside the permitted working directory'
    #     )
    #     self.assertEqual(expected, output)

    # def test_above(self):
    #     output = get_files_info("calculator", "../")
    #     expected = (
    #         'Error: Cannot list "../" as it is outside the permitted working directory'
    #     )
    #     self.assertEqual(expected, output)

    # def test_max_chars(self):
    #     file_path = "lorem.txt"
    #     output = get_file_content("calculator", file_path)
    #     warning_msg = MAX_CHARS_ERROR_MSG_TEMPLATE.format(
    #         file_path=file_path, max_chars=MAX_CHARS_FROM_FILE
    #     )
    #     print(output)
    #     self.assertEqual(True, len(output) <= MAX_CHARS_FROM_FILE + len(warning_msg))

    # def test_main(self):
    #     file_path = "main.py"
    #     output = get_file_content("calculator", file_path)
    #     warning_msg = MAX_CHARS_ERROR_MSG_TEMPLATE.format(
    #         file_path=file_path, max_chars=MAX_CHARS_FROM_FILE
    #     )
    #     print(output)
    #     self.assertEqual(True, len(output) <= MAX_CHARS_FROM_FILE + len(warning_msg))

    # def test_pkg_calc(self):
    #     file_path = "pkg/calculator.py"
    #     output = get_file_content("calculator", file_path)
    #     warning_msg = MAX_CHARS_ERROR_MSG_TEMPLATE.format(
    #         file_path=file_path, max_chars=MAX_CHARS_FROM_FILE
    #     )
    #     print(output)
    #     self.assertEqual(True, len(output) <= MAX_CHARS_FROM_FILE + len(warning_msg))

    # def test_bin_cat(self):
    #     file_path = "/bin/cat"
    #     output = get_file_content("calculator", file_path)
    #     warning_msg = MAX_CHARS_ERROR_MSG_TEMPLATE.format(
    #         file_path=file_path, max_chars=MAX_CHARS_FROM_FILE
    #     )
    #     print(output)
    #     self.assertEqual(True, len(output) <= MAX_CHARS_FROM_FILE + len(warning_msg))

    # def test_does_not_exist(self):
    #     file_path = "pkg/does_not_exist.py"
    #     output = get_file_content("calculator", file_path)
    #     warning_msg = MAX_CHARS_ERROR_MSG_TEMPLATE.format(
    #         file_path=file_path, max_chars=MAX_CHARS_FROM_FILE
    #     )
    #     print(output)
    #     self.assertEqual(True, len(output) <= MAX_CHARS_FROM_FILE + len(warning_msg))

    # def test_lorem(self):
    #     output = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    #     print(output)
    #     self.assertEqual(True, "wait" in get_file_content("calculator", "lorem.txt"))

    # def test_morelorem(self):
    #     output = write_file(
    #         "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
    #     )
    #     print(output)
    #     self.assertEqual(
    #         True, "amet" in get_file_content("calculator", "pkg/morelorem.txt")
    #     )

    # def test_tmp_temp(self):
    #     output = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    #     print(output)
    #     self.assertEqual(
    #         True, "Error" in get_file_content("calculator", "/tmp/temp.txt")
    #     )

    def test_main(self):
        output = run_python_file("calculator", "main.py")
        print(output)
        self.assertEqual(True, 'Example: python main.py "3 + 5"' in output)

    def test_main_args(self):
        output = run_python_file("calculator", "main.py", ["3 + 5"])
        print(output)
        self.assertEqual(True, "8" in output)

    def test_test(self):
        output = run_python_file("calculator", "tests.py")
        print(output)
        self.assertEqual(True, "OK" in output)

    def test_above(self):
        output = run_python_file("calculator", "../main.py")
        print(output)
        self.assertEqual(True, "Error" in output)

    def test_nonexistent(self):
        output = run_python_file("calculator", "nonexistent.py")
        print(output)
        self.assertEqual(True, "Error" in output)

    def test_lorem(self):
        output = run_python_file("calculator", "lorem.txt")
        print(output)
        self.assertEqual(True, "Error" in output)


if __name__ == "__main__":
    unittest.main()
