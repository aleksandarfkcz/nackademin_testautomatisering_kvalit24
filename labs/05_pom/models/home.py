import re
from playwright.sync_api import expect

class HomePage:
    def __init__(self, page):
        self.page = page

    def verify_homepage_loaded(self):
        expect(self.page.get_by_text("Nackademin Course App")).to_be_visible()

    def add_product(self, product_name: str):
        self.page.get_by_placeholder("Product Name").fill(product_name)
        self.page.get_by_role("button", name=re.compile("Create Product", re.I)).click()
        expect(self.page.locator(".product-item", has_text=product_name)).to_be_visible(timeout=3000)

    def delete_product(self, product_name: str):
        item = self.page.locator(".product-item", has_text=product_name)
        item.get_by_role("button", name="Delete").click()
        expect(self.page.locator(".product-item", has_text=product_name)).to_have_count(0)