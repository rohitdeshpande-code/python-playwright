from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils


def intercept_request(route):

    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=693c144332ed8658712f3e07")



def test_network_2(page: Page):

    page.goto("https://rahulshettyacademy.com/client/", wait_until="domcontentloaded")

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)

    page.get_by_placeholder("email@example.com").fill("rdtest01@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("PassworD@2025")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()

    message = page.locator('.blink_me').text_content()
    print(message)


def test_session_storage(playwright: Playwright):

    api_utils = APIUtils()
    getToken = api_utils.getToken(playwright)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()

    #script to inject token in local session storage
    page.add_init_script(f"""localStorage.setItem('token', '{getToken}')""")
    page.goto('https://rahulshettyacademy.com/client/', wait_until="domcontentloaded")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()




