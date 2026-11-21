from playwright.sync_api import Page, expect
import time

def test_Alert1(page: Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_text("Click for JS Alert").click()
    time.sleep(3)

def test_getSuggestions(page: Page):
    page.goto("https://www.bing.com/")
    page.locator(".sb_form_q").fill("selenium")
    time.sleep(5)

    suggestionsText = page.locator(".sa_tm").locator(".pp_title").all_inner_texts()
    for suggestions in suggestionsText:
        print(suggestions)

    time.sleep(3)

    