from .ordersHistory import ordersHistoryPage


class DashBoardPage:

    def __init__(self, page):
        self.page = page

    def selectOrdersNavLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        ordershistoryPage = ordersHistoryPage(self.page)
        return ordershistoryPage