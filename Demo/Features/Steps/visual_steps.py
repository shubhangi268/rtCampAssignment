import os
from behave import then
from behave.api.async_step import async_run_until_complete
from Demo.Features.Pages.inventory_page import InventoryPage

@then("User should capture a visual snapshot of the inventory page")
@async_run_until_complete
async def screenshot(context):
    print("Capturing visual snapshot of inventory page...")
    os.makedirs("snapshots", exist_ok=True)  # Create snapshots folder if it does not exists
    inventory_page = InventoryPage(context.page)
    await inventory_page.take_screenshot("snapshots/inventory.png")
    print("Snapshot captured successfully.")