import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils


scenarios('features/orderTransaction.feature')
@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {} #dictionary
    user_credentials['userEmail'] = username
    user_credentials['userPassword'] = password


    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)
    shared_data['order_id'] = orderId


@given('the user is on landing page')
def user_on_landing_page(browserInstance, shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    shared_data["login_page"] = loginPage

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    loginPage = shared_data["login_page"]
    dashboardPage = loginPage.login(username, password)
    shared_data["dashboard_page"] = dashboardPage


@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboardPage = shared_data["dashboard_page"]
    ordershistoryPage = dashboardPage.selectOrdersNavLink()
    shared_data['ordershistory_page'] = ordershistoryPage

@when('select the order Id')
def select_order_id(shared_data):
    ordershistoryPage = shared_data['ordershistory_page']
    orderId = shared_data['order_id']
    orderdetailsPage = ordershistoryPage.selectOrder(orderId)
    shared_data['orderdetails_page'] = orderdetailsPage


@then('order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    orderdetailsPage = shared_data['orderdetails_page']
    orderdetailsPage.verifyOrderMessage()