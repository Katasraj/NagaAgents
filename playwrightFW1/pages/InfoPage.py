from playwright.sync_api import Page,expect
from playwrightFW1.utilities.random_data import RandomData

class InfoPage:
    def __init__(self,page:Page):
        self.page = page
        self.first_Name_field = page.get_by_placeholder("First Name")
        self.last_Name_field = page.get_by_placeholder("Last Name")
        self.postalcode_field = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("#continue")

    def enter_checkout_information(self):
        random_data = RandomData()
        self.first_Name_field.fill(random_data.get_first_name())
        self.last_Name_field.fill(random_data.get_last_name())
        self.postalcode_field.fill(random_data.get_zipcode())

        self.page.wait_for_timeout(4000)
        self.continue_button.click()



