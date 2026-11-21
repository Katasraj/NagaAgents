from playwright.sync_api import Page, expect
from playwrightFW1.utilities.configReader import ConfigFileReader

class HomePage:
    def __init__(self,page:Page):
        self.page = page
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.shopping_cart_icon = page.locator(".shopping_cart_link")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_lonk = page.get_by_role("button", name="Logout")


    def add_first_product_to_cart(self):
        self.add_to_cart_button.first.click()
        self.shopping_cart_icon.first.click()
        config_file_reader = ConfigFileReader()
        cart_url = config_file_reader.readConfig("basic info","cartURL")
        expect(self.page).to_have_url(cart_url)

    def logout_from_application(self):
        self.menu_button.click()
        self.logout_lonk.click()

