from playwright.sync_api import Page
import time


def test_WebTable1(page: Page):
    page.goto("https://www.w3schools.com/html/html_tables.asp")
    value1 = page.locator("//tr[2]/td[1]").first.inner_text()
    print("VALUE 1: ", value1)

    value2 = page.locator("//tr[2]/td[2]").first.inner_text()
    print("VALUE 2: ", value2)

    value3 = page.locator("//tr[2]/td[3]").first.inner_text()
    print("VALUE 3: ", value3)


def test_WebTable2(page: Page):
    page.goto("https://www.w3schools.com/html/html_tables.asp")
    tableRows = page.locator("#customers").get_by_role("row")

    value1 = tableRows.nth(1).locator("//td[1]").inner_text()
    print("VALUE 1: ", value1)

    value2 = tableRows.nth(2).locator("//td[1]").inner_text()
    print("VALUE 2: ", value2)

    value3 = tableRows.nth(3).locator("//td[1]").inner_text()
    print("VALUE 3: ", value3)