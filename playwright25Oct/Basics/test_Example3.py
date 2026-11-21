import time

from playwright.sync_api import Page, expect

# Id = “searchBox” , #id —> css for that element
# class= “classname” , .classname —> for that element
# placeholder= “enter name” , [placeholder=‘value’]
# .classname[attribute=‘value’]

def test_cssExample(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    time.sleep(3)
    page.locator(".submit-button").click()


def test_handleShadowElement(page: Page):
    page.goto("https://developer.salesforce.com/")
    # page.get_by_text("Try for free").last.click()
    page.locator("hgf-button", has_text="Try for free").last.click()
    time.sleep(5)

def test_filterLOcation(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    time.sleep(5)
    page.locator(".inventory_item").filter(has_text="Sauce Labs Bolt T-Shirt").get_by_role("button", name="Add to cart").click()
    time.sleep(5)

def test_HardAssertions(page: Page):
    page.goto("https://www.saucedemo.com/")
    #expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page).to_have_url("https://www.leby.com/")
    expect(page).to_have_title("Swag Labs")
    expect(page).not_to_have_title("Suren")


def test_SoftAssertions2(page: Page):
    page.goto("https://www.saucedemo.com/")
    expect(page).soft(page).to_have_url("https://www.leby.com/")
    expect(page).soft(page).to_have_title("Swag Labs")

