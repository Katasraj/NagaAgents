from playwright.sync_api import Page
import time
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
# wd = os.getcwd()




def test_FileUploading1(page: Page):
    file_path = BASE_DIR / "data1.txt"
    print("FILE PATH: ",file_path)
    print("TYPE: ", type(file_path))
    page.goto("https://the-internet.herokuapp.com/upload")
    time.sleep(3)
    page.locator("#file-upload").set_input_files(str(file_path))
    time.sleep(10)