from behave import when, then
from behave.api.async_step import async_run_until_complete
from Demo.Features.Pages.checkout_page import CheckoutPage

@when("User add multiple items to the cart and checkout")
@async_run_until_complete
async def add_items(context):
    print("Adding multiple items to the cart...")
    checkout_page = CheckoutPage(context.page)
    await checkout_page.add_items_to_cart()  # await method call
    await checkout_page.checkout()           # await method call

@then("User should complete the purchase successfully")
@async_run_until_complete()
async def complete_checkout(context):
    print("Verifying the purchase completion...")
    # getting the checkout completion page
    await context.page.wait_for_url("**/checkout-complete.html")
    assert "checkout-complete" in context.page.url, "Checkout not completed successfully."
    print("Purchase completed successfully.")