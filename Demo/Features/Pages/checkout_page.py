class CheckoutPage:
    def __init__(self, page):
        self.page = page

    # Method to add multiple items to the cart
    async def add_items_to_cart(self, count=3):
        print(f"Adding {count} items to cart...")

        buttons = await self.page.query_selector_all("button.btn_inventory")
        print("Total no. of items >>>>>>", len(buttons))
        for btn in buttons[:count]:
            await btn.click()  #it is clicking on the Add to Cart button

    # Method to complete the checkout process
    async def checkout(self):
        print("Proceeding to checkout...")
        await self.page.click(".shopping_cart_link") #clicking on the cart
        await self.page.click("#checkout")  # Clicking the Checkout button

        # Filling the checkout information
        await self.page.fill("#first-name", "Shubhangi")
        await self.page.fill("#last-name", "Testing")
        await self.page.fill("#postal-code", "12345")

        await self.page.click("#continue")  # Clicking on the Continue button

        await self.page.click("#finish")  # Clicking on the Finish button
        print("Checkout process completed successfully.")