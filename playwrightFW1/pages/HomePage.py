from playwright.sync_api import Page, expect

from playwrightFW1.utilities import configReader
from playwrightFW1.utilities.configReader import ConfigFileReader

class HomePage:
    def __init__(self,page:Page):
        self.page = page
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.shopping_cart_icon = page.locator(".shopping_cart_link")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_lonk = page.get_by_role("button", name="Logout")
        self.about_link = page.locator("#about_sidebar_link")
        self.all_products_title = page.locator(".inventory_item_name ")
        self.product_description = page.locator(".inventory_details_desc")


    def add_first_product_to_cart(self):
        try:
            self.add_to_cart_button.first.click()
            self.shopping_cart_icon.first.click()
            config_file_reader = ConfigFileReader()
            cart_url = config_file_reader.readConfig("basic info","cartURL")
            expect(self.page).to_have_url(cart_url)
        except:
            print("Error occured when adding product to the cart")

    def logout_from_application(self):
        try:
            self.menu_button.click()
            self.logout_lonk.click()
        except:
            print("Error occured when logging out from the application")


    def verify_about_page(self):
        try:
            self.menu_button.click()
            self.about_link.click()
            config_file_reader = ConfigFileReader()
            about_URL = config_file_reader.readConfig(
                "basic info","aboutURL")
            self.page.wait_for_timeout(4000)
            expect(self.page).to_have_url(about_URL)
            self.page.go_back()
        except:
            print("Error occured when verifying about page")

    def navigate_to_products_list(self):
        try:
           for product in self.all_products_title.all():
               product.click()
               expect(self.product_description).to_be_visible()
               print(self.product_description.inner_text())
               self.page.wait_for_timeout(5000)
               self.page.go_back()

        except:
            print("Error occured when navigating to products page")


