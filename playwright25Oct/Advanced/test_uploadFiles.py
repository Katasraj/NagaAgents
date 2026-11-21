from playwright.sync_api import Page, expect
import time
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
# wd = os.getcwd()
"""
Why use Path(__file__).resolve().parent instead of a hardcoded path?

Because it dynamically identifies the current Python file's directory, making the application more portable and reducing 
path-related errors.

One important distinction: Path(__file__).resolve().parent identifies the directory containing the Python file, 
not necessarily the directory from which you execute the program
"""


def test_FileUploading1(page: Page):

    file_path_1 = BASE_DIR / "data1.txt"
    file_path_2 = BASE_DIR / "Data2.txt"
    page.goto("https://www.file.io/")
    time.sleep(3)
    page.locator("//label[@for='select-files-input']").set_input_files([str(file_path_1), str(file_path_2)])
    time.sleep(10)


    """Scenario 1"""
    # file_path = BASE_DIR / "data1.txt"
    # print("FILE PATH: ",file_path)
    # print("TYPE: ", type(file_path))
    # assert file_path.exists(), f"Missing file: {file_path}"
    #
    # page.goto("https://the-internet.herokuapp.com/upload")
    # time.sleep(3)
    # page.locator("#file-upload").set_input_files(str(file_path))
    # time.sleep(3)
    # page.locator("#file-submit").click()
    # time.sleep(3)
    # expect(page.locator("#uploaded-files")).to_have_text(file_path.name)


