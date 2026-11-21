from playwright.sync_api import Page,expect
from playwrightFW1.utilities.configReader import ConfigFileReader


class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username_textField = page.get_by_role("textbox", name="Username")
        self.password_textField = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")


    def login_to_application(self, username,password):
        self.username_textField.fill(username)
        self.password_textField.fill(password)
        self.login_button.click()
        config_file_reader = ConfigFileReader()

        bashboard_URL = config_file_reader.readConfig("basic info","dashboardURL")
        self.page.wait_for_url(bashboard_URL)
        expect(self.page).to_have_url(bashboard_URL)

        
