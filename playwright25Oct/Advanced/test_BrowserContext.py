import time


def test_AuthLogin(page):
    page.locator("#user-name").fill("admin")
    page.locator("#password").fill("admin")
    time.sleep(10)