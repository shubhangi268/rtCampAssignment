from playwright.async_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    # Async method to select a sorting option
    async def sort_by(self, option):
        print("Sorting in progress...")
        await self.page.select_option("select.product_sort_container", value=option)  # Async select option
        print('Sorting done....')

    # Async method to get all item names on the page
    async def get_item_names(self):
        # Using await for async retrieval of item names

        elements = await self.page.query_selector_all(".inventory_item_name")
        return [await el.inner_text() for el in elements]  # fetching inner_text of each product

    # Async method to get all item prices on the page
    async def get_item_prices(self):
        # Use await for async retrieval of item prices
        elements = await self.page.query_selector_all(".inventory_item_price")
        return [float((await el.inner_text()).strip("$")) for el in elements] # fetching the inner_text of the price

    # Async method to take a full-page screenshot
    async def take_screenshot(self, path):
        await self.page.screenshot(path=path, full_page=True)  #taking the screenshot