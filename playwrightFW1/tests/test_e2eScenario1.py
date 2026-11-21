from playwrightFW1.pages.HomePage import HomePage
from playwrightFW1.pages.loginPage import LoginPage
from playwrightFW1.pages.cartPage import CartPage
from playwrightFW1.pages.InfoPage import InfoPage
from playwrightFW1.utilities.ExcelData import ExcelUtility
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # playwrightFW1
CONFIG_PATH = os.path.join(BASE_DIR, "testData", "userinfo.xlsx")

def test_firstscript(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    cart_page = CartPage(page)
    info_page = InfoPage(page)
    excel_utility = ExcelUtility()

    username = excel_utility.getCellData(CONFIG_PATH,"Sheet1",2,1)
    password = excel_utility.getCellData(CONFIG_PATH,"Sheet1",2,2)

    login_page.login_to_application(username, password)
    home_page.add_first_product_to_cart()
    cart_page.proceed_to_checkout()
    info_page.enter_checkout_information()
    home_page.logout_from_application()


