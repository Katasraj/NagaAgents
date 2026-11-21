from playwright.sync_api import Page,expect

from playwright25Oct.Basics.first_program import page


class CartPage:
    def __init__(self,page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")

    def proceed_to_checkout(self):
        self.checkout_button.click()


