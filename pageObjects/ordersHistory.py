from .orderDetails import orderDetailsPage


class ordersHistoryPage:

    def __init__(self, page):
        self.page = page

    def selectOrder(self, orderId):
        row = self.page.locator('tr').filter(has_text=orderId)
        row.get_by_role("button", name='View').click()
        orderdetailsPage = orderDetailsPage(self.page)
        return orderdetailsPage

