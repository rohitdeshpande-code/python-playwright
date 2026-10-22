from .dashboard import DashBoardPage


class LoginPage:

    def __init__(self, page):
        self.page = page


    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client", wait_until="domcontentloaded")

    def login(self, userEmail, userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.get_by_role("button", name="Login").click()
        dashboardPage = DashBoardPage(self.page)
        return dashboardPage