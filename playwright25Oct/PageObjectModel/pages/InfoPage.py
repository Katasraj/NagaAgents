from playwright.sync_api import Page,expect

class InfoPage:
    def __init__(self,page:Page):
        self.page = page
        self.first_Name_field = page.get_by_placeholder("First Name")
        self.last_Name_field = page.get_by_placeholder("Last Name")
        self.postalcode_field = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("#continue")

    def enter_checkout_information(self,firstName,lastName,zipPostalCode):
        self.first_Name_field.fill(firstName)
        self.last_Name_field.fill(lastName)
        self.postalcode_field.fill(zipPostalCode)
        self.continue_button.click()



