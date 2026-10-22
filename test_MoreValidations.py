import time

from playwright.sync_api import Page, expect

def test_UIChecks(page: Page):

    # hide/display and placeholder
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name = "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #Alertboxes
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name = "Confirm").click()
    time.sleep(4)

    #Mousehover
    page.locator('#mousehover').hover()
    page.get_by_role("link", name="Top").click()

    #Frame Handeling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name = "All Access plan").click()
    #expect(pageFrame.locator('body')).to_contain_text("Happy Subscribers")

    #Check the price of rice equal to is 37
    #identify the price column
    #identify the rice row
    #extract the price of rice

    page.goto("https://rahulshettyacademy.com/seleniumPractice/#/offers")

    for index in range(page.locator('th').count()):
        if page.locator('th').nth(index).filter(has_text="Price").count() > 0:
            priceColIndex = index
            print(f"Price column value is {priceColIndex} ")
            break

    riceRow = page.locator('tr').filter(has_text="Rice")
    expect(riceRow.locator('td').nth(priceColIndex)).to_have_text('37')


