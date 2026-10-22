import json
from pathlib import Path

#python --browser_name chrome -m smoke -n 3 --tracing on --html=reporter.html

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from utils.apiBaseFramework import APIUtils

#json file -> utils -> access into test (converts json into python object)
CREDENTIALS_PATH = Path(__file__).parent / 'data' / 'credentials.json'
with open(CREDENTIALS_PATH) as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, browserInstance, user_credentials):

    userEmail = user_credentials["userEmail"]
    userPassword = user_credentials["userPassword"]

    #create order -> orderId
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)

    #login
    loginPage = LoginPage(browserInstance) #object for login page class
    loginPage.navigate()

    dashboardPage = loginPage.login(userEmail, userPassword)

    ordershistoryPage = dashboardPage.selectOrdersNavLink()

    orderdetailsPage = ordershistoryPage.selectOrder(orderId)
    orderdetailsPage.verifyOrderMessage()
