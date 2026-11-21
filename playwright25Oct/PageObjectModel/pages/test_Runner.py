from playwright.sync_api import Page, expect
from random_data import RandomData


def test_Runner(page: Page):
    randomData = RandomData()
    page.goto("https://www.saucedemo.com/")

    fname = randomData.get_first_name()
    page.get_by_placeholder("Username").fill(fname)
    page.wait_for_timeout(4800)
