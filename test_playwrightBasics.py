import time

from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")

#chromium headless mode, 1 single context
def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com/")

#css selectors we can use - if id is there then #id, if class is there then .class
def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    #page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_label("password").fill("learning123")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    #time.sleep(5)

def firefoxBrowser(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    # page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_label("password").fill("learning123")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()

    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
