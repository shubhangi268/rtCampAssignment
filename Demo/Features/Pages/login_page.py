from playwright.async_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.userName = self.page.locator("#user-name")  # Locator for username textfield
        self.password = self.page.locator("#password")  # Locator for password textfield
        self.loginBtn = self.page.locator("#login-button")  # Locator for login button

    # Method to login into the application
    async def login(self, userName, password):
        print(f"Logging in with username: {userName}")
        await self.page.goto("https://www.saucedemo.com/")  # Navigate to the application
        await self.userName.fill(userName)  # Fill in the username field
        await self.password.fill(password)  # Fill in the password field
        await self.loginBtn.click()  # Click on the login button
        print("User logged in successfully...!!!")