from playwright.sync_api import Playwright

orderPayLoad = {"orders": [{"country": "Cuba", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}

class APIUtils:

    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com", ignore_https_errors=True)
        response = api_request_context.post("/api/ecom/auth/login",
                                 data={"userEmail": "rdtest01@gmail.com", "userPassword": "PassworD@2025"})

        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]


    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com", ignore_https_errors=True)
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data=orderPayLoad,
                                 headers = {"Authorization": token,
                                            "Content-Type": "application/json"
                                            })

        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId
