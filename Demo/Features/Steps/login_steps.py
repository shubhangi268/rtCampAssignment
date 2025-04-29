from behave import given
from behave.api.async_step import async_run_until_complete
from playwright.async_api import async_playwright, expect

from Demo.Features.Pages.login_page import LoginPage

# Defining valid username and password
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@given("User logged into Saucedemo application")
@async_run_until_complete
async def login(context):
    #Starting Playwright
    context.playwright = await async_playwright().start()
    #Launching the browser
    context.browser = await context.playwright.chromium.launch(headless=True, slow_mo=1000)
    # Opening a new web browser
    context.page = await context.browser.new_page()

    # Creating LoginPage object and performing login
    login_page = LoginPage(context.page)
    await login_page.login(USERNAME, PASSWORD)

    #wait and check if current page url is matching
    await expect(context.page).to_have_url("https://www.saucedemo.com/inventory.html")

    print("User Logged in Successfully...!!!")
