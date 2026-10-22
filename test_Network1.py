import pytest
from playwright.sync_api import Page

fakePayLoadOrders = {"data":[],"message":"No Orders"}


# api call from browser -> api call contact server return back response to browser -> browser use response to generate html

def intercept_response(route):
    route.fulfill(
        json = fakePayLoadOrders
    )


@pytest.mark.smoke
def test_Network_1(page: Page):

    page.goto("https://rahulshettyacademy.com/client/", wait_until="domcontentloaded")

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-cutomers/*", intercept_response)

    page.get_by_placeholder("email@example.com").fill("rdtest01@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("PassworD@2025")
    page.get_by_role("button", name = "Login").click()
    page.get_by_role("button", name="ORDERS").click()

    order_text = page.locator('.mt-4').text_content()
    print(order_text)


