import pytest
from playwrightFW1.pages.HomePage import HomePage
from playwrightFW1.pages.loginPage import LoginPage
from playwrightFW1.pages.cartPage import CartPage
from playwrightFW1.pages.InfoPage import InfoPage
from playwrightFW1.utilities.ExcelData import ExcelUtility
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # playwrightFW1
CONFIG_PATH = os.path.join(BASE_DIR, "testData", "userinfo.xlsx")

"""@pytest.mark.usefixtures("page") tells pytest to run the page fixture for every test in the class, 
even if the test doesn't list page as a parameter."""


@pytest.mark.usefixtures("page")
class TestE2EScenarios:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.cart_page = CartPage(page)
        self.info_page = InfoPage(page)
        self.excel_utility = ExcelUtility()

    @pytest.mark.smoke
    def test_e2eScenario1(self,page):
        username = self.excel_utility.getCellData(CONFIG_PATH, "Sheet1", 2, 1)
        password = self.excel_utility.getCellData(CONFIG_PATH, "Sheet1", 2, 2)

        self.login_page.login_to_application(username, password)
        self.home_page.add_first_product_to_cart()
        self.cart_page.proceed_to_checkout()
        self.info_page.enter_checkout_information()
        self.home_page.logout_from_application()

    @pytest.mark.smoke
    def test_e2eScenario2(self,page):
        username = self.excel_utility.getCellData(CONFIG_PATH, "Sheet1", 2, 1)
        password = self.excel_utility.getCellData(CONFIG_PATH, "Sheet1", 2, 2)

        self.login_page.login_to_application(username, password)
        self.home_page.verify_about_page()
        self.home_page.logout_from_application()

    @pytest.mark.regression
    def test_e2eScenario3(self,page):

        username = self.excel_utility.getCellData(CONFIG_PATH, "Sheet1", 2, 1)
        password = self.excel_utility.getCellData(CONFIG_PATH, "Sheet1", 2, 2)

        self.login_page.login_to_application(username, password)
        self.home_page.navigate_to_products_list()
        self.home_page.logout_from_application()

