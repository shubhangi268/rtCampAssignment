from behave import when, then
from behave.api.async_step import async_run_until_complete
from Demo.Features.Pages.inventory_page import InventoryPage

@when("User sort products by name from Z to A")
@async_run_until_complete
async def sort_names_z_to_a(context):
    print("Sorting products by name from Z to A...")
    inventory_page = InventoryPage(context.page)
    await inventory_page.sort_by("za")  # Await the sorting action asynchronously

@then("User should see the items sorted in descending order")
@async_run_until_complete
async def get_names_sorted(context):
    names = await InventoryPage(context.page).get_item_names() #fetching the item names
    assert names == sorted(names, reverse=True)

@when("User sort products by price from high to low")
@async_run_until_complete
async def sort_price_high_low(context):
    print("Sorting products by price from high to low...")
    inventory_page = InventoryPage(context.page)
    await inventory_page.sort_by("hilo")


@then("User should see the items sorted by descending price")
@async_run_until_complete
async def get_prices_sorted(context):
    prices = await InventoryPage(context.page).get_item_prices() #fetching the prices of item
    assert prices == sorted(prices, reverse=True)
