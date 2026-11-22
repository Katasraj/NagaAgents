from playwright.sync_api import Page,expect
from playwrightFW1.utilities.configReader import ConfigFileReader


class CartPage:
    def __init__(self,page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")

    def proceed_to_checkout(self):
        try:
            configReader = ConfigFileReader()
            self.checkout_button.click()
            yourInfo_URL = configReader.readConfig("basic info","yourInfoURL")
            expect(self.page).to_have_url(yourInfo_URL)
        except:
            print("Error occured while proceeding to checkout")

