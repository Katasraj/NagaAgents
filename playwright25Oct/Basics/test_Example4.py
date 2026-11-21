import time
from playwright.sync_api import Page, expect

def test_getTextFromButton(page:Page):
    page.goto("https://www.makemytrip.com/")
    vale = page.get_by_role("button", name="Fast Track Immigration").inner_text()
    print("button text: ",vale)

def test_HandleCheckBoxes(page:Page):
    page.goto("https://www.bing.com/account/general?ru")
    expect(page.get_by_role("checkbox", name="Search suggestions")).to_be_checked()
    page.get_by_role("checkbox", name="Search suggestions").uncheck()
    time.sleep(3)
    expect(page.get_by_role("checkbox", name="Search suggestions")).not_to_be_checked()
    page.get_by_role("checkbox", name="Search suggestions").check()
    time.sleep(3)
    expect(page.get_by_role("checkbox", name="Search suggestions")).to_be_checked()


def test_MultipleCheckboxes(page:Page):
    page.goto("https://www.bing.com/account/general?ru")
    checkboxes = page.get_by_role("checkbox")
    print("checkboxes: ",checkboxes.count())



