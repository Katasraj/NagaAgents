from playwright.sync_api import Page, expect
import time

def test_doubleclick(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#login-button").dblclick()  # Double click
    time.sleep(3)

def test_rightclick(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("#login-button").click(button="right")  # right click
    time.sleep(3)

def test_Frames1(page: Page):
    page.goto("https://jqueryui.com/tooltip/")
    frame1 = page.frame(url="https://jqueryui.com/resources/demos/tooltip/default.html")
    frame1.locator("#age").fill("25")
    time.sleep(3)

def test_Handling_ChildFrames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")
    frame1 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3.html")
    frame1.locator("//input[@name='mytext3']").fill("surendra")

    frame2 = frame1.child_frames
    frame2[0].locator('//*[@id="i6"]/div[3]/div').click()

    time.sleep(3)

def test_HandlingToolTip(page:Page):
    page.goto("https://jqueryui.com/tooltip/")
    frame1 = page.frame_locator(".demo-frame")
    tooltipMessage = frame1.locator("#age").get_attribute("title")
    print("TooltipMessage: ", tooltipMessage)
    time.sleep(5)

def test_DragDrop(page:Page):
    page.goto("https://jqueryui.com/droppable/")
    frame1 = page.frame_locator(".demo-frame")

    '''Approach 1'''
    # source = frame1.locator("#draggable")
    # destination = frame1.locator("#droppable")
    # source.drag_to(destination)
    # time.sleep(3)

    '''Approach 2'''
    frame1.locator("#draggable").hover()
    page.mouse.down()
    frame1.locator("#droppable").hover()
    page.mouse.down()
    time.sleep(3)

def test_DatePicker1(page:Page):
    page.goto("https://jqueryui.com/datepicker/")
    frame1 = page.frame_locator(".demo-frame")

    '''Approach 1'''
    # frame1.locator("#datepicker").click()
    # frame1.locator(".ui-icon-circle-triangle-e").click()
    # frame1.get_by_text("16").click()
    # time.sleep(3)

    '''Approach 2''' # Selecting current date
    frame1.locator("#datepicker").click()
    frame1.locator("//td[@class=' ui-datepicker-days-cell-over  ui-datepicker-today']//a").click()
    time.sleep(3)


