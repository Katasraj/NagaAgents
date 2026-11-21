from playwright.sync_api import Page, expect
from loginPage import LoginPage
from HomePage import HomePage
from cartPage import CartPage
from InfoPage import InfoPage
#from playwright25Oct.utils.generate_logs import Logging
from utils.generate_logs import Logging

logger = Logging().log("sausedemo")


def test_scenario1(page: Page):
    logger.info("Starting test_scenario1")
    try:
        page.goto("https://www.saucedemo.com/")
        logger.info("Opened saucedemo.com")

        login_page = LoginPage(page)
        login_page.login_to_application("standard_user", "secret_sauce")
        logger.info("Logged in as standard_user")

        home_page = HomePage(page)
        home_page.add_first_product_to_cart()
        logger.info("Added first product to cart")

        cart_page = CartPage(page)
        cart_page.proceed_to_checkout()
        logger.info("Proceeded to checkout")

        info_page = InfoPage(page)
        info_page.enter_checkout_information("suren", "Jag", "500032")
        logger.info("Entered checkout information")

        page.wait_for_timeout(4000)
        home_page.logout_from_application()
        logger.info("Logged out - test passed")
    except Exception:
        logger.exception("test_scenario1 failed")
        raise
