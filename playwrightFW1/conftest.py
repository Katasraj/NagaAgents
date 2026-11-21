import pytest

@pytest.fixture(scope="function")
def browser_context(playwright,browser_context_args):
    browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context()  # isolated browser context
    yield context       # PAUSE here, hand context to the next step
    context.close()     # runs only after the test finishes
    browser.close()

"""yield means "give this to the test and wait". The lines below it don't run until the test is completely done."""

@pytest.fixture(scope="function")
def page(browser_context, base_url):
    page = browser_context.new_page()
    page.goto(base_url)
    yield page
    page.close()

"""
Function 1: browser_context

"Open Chrome."
- It launches the Chrome window.
- It gives you a clean, fresh session with no old cookies or logins.
- After the test, it closes Chrome.

Function 2: page

"Open a new tab and go to the website."
- It uses the Chrome window from function 1.
- It opens a tab and goes to your website URL (base_url).
- After the test, it closes the tab.

What happens when you run a test

def test_login(page):
    page.fill("#user", "admin")
1. The test asks for page.
2. page needs browser_context, so Chrome opens first.
3. Then a tab opens and loads your website.
4. Your test steps run.
5. Cleanup: the tab closes, then Chrome closes.

In one line each

- browser_context: opens and closes the browser.
- page: opens and closes the tab, and loads the site.



The browser in function 1 does not close before function 2 runs. Function 2 doesn't open another browser. 
It reuses the one from function 1.

Why: yield pauses the function

def browser_context(...):
    browser = launch()      # runs first
    context = new_context()
    yield context           # PAUSE here, hand context to the next step
    context.close()         # runs only after the test finishes
    browser.close()
yield means "give this to the test and wait". The lines below it don't run until the test is completely done.

Actual order

1. browser_context runs: Chrome opens. It pauses at yield, and Chrome stays open.
2. page runs and receives that same context: it opens a tab in the same Chrome and loads the site.
3. The test runs.
4. Teardown, in reverse: page closes the tab, then browser_context resumes after its yield and closes Chrome.

Purpose of the first function

It provides the browser session that the tab lives in. A tab can't exist without a browser and context, 
so page depends on browser_context.

Only one browser opens per test. The second function just adds a tab to it.
"""