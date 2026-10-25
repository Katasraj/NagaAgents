import re
import time

from playwright.sync_api import Page, expect


def test_example2(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()


def test_example3(page:Page):
    page.goto("https://www.salesforce.com/form/developer-signup/?d=pb")
    page.get_by_label("First name").fill("suren")
    page.get_by_label("Last name").fill("jagan")
    page.get_by_label("Job title").fill("developer")
    page.get_by_label("Company").fill("adb")
    page.get_by_label("Work email").fill("suren@gmail.com")


def test_example4(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_placeholder("Job title").fill("developer")

def test_example5(page:Page):
    page.goto("https://jqueryui.com/tooltip")
    page.get_by_title("jQuery UI").first.click()
    time.sleep(3)

def test_example6(page:Page):
    page.goto("https://www.bing.com/?toWww=1&redig=F2A18834747840F38F6B261760D6C2E4")
    page.get_by_alt_text("© India.com").first.click()
    time.sleep(3)