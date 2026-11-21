from playwright.sync_api import Page


def test_autowait_1(page: Page):
    page.goto("http://uitestingplayground.com/ajax")
    page.locator("#ajaxButton").click()
    page.wait_for_timeout(20000)
    message = page.locator(".bg-success").inner_text()
    assert message == "Data loaded with AJAX get request."


def test_autowait_2(page: Page):
    page.goto("http://uitestingplayground.com/ajax")
    page.locator("#ajaxButton").click()
    page.locator(".bg-success").wait_for(state="visible")
    message = page.locator(".bg-success").inner_text()
    assert message == "Data loaded with AJAX get request."


def test_autowait_3(page: Page):
    page.goto("http://uitestingplayground.com/ajax")
    page.locator("#ajaxButton").click()
    page.wait_for_selector(".bg-success")
    message = page.locator(".bg-success").all_text_contents()
    print(message)