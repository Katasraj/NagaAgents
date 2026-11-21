from playwright.sync_api import Page,expect
import time

def test_usere2eflow(page: Page):
    page.goto("https://www.saucedemo.com/")
    # Loginto application
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # Add product to cart
    page.get_by_role("button", name="Add to cart").first.click()
    page.locator(".shopping_cart_link").click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    # Checkout
    page.get_by_role("button", name="checkout").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    page.get_by_placeholder("First Name").fill("suren")
    page.get_by_placeholder("Last Name").fill("jag")
    page.get_by_placeholder("Zip/Postal Code").fill("500032")
    page.locator("#continue").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    # Finish
    page.get_by_role("button", name="finish").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    time.sleep(3)

    # Backto Home
    page.get_by_role("button", name="Back Home").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    time.sleep(3)








