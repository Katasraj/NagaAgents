from playwright.sync_api import Page,expect




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
        
