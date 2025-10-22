import re
import time
from playwright.sync_api import Page, expect

# ---------------------- CONFIGS ------------------------------
BASE_URL = "http://localhost:5173/"
admin_user = "admin" # user name dont work
admin_pass = "123456789" # pass dont work
# admin_user = "admin1" 
# admin_pass = "admin123456789"
random_product = f"prod_{int(time.time())}"

# ---------------------- HELPERS ------------------------------

def do_login(page: Page, username: str, password: str):
    page.goto(BASE_URL, wait_until="networkidle")
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Login").click()

    
    # expect(page.get_by_role("button", name=re.compile("(Create Product|Add Product)", re.I))).to_be_visible(timeout=5000)

def add_product(page: Page, product_name: str):
    page.get_by_placeholder("Product Name").fill(product_name)
    page.get_by_role("button", name=re.compile("Create Product", re.I)).click()
    # Bekräfta att produkten syns i listan
    expect(page.locator(".product-item", has_text=product_name)).to_be_visible(timeout=3000)

def delete_product(page: Page, product_name: str):
    item = page.locator(".product-item", has_text=product_name)
    item.get_by_role("button", name="Delete").click()
    expect(page.locator(".product-item", has_text=product_name)).to_have_count(0)

# ---------------------- TESTS ------------------------------
def test_admin_can_add_and_delete(page: Page):
    do_login(page, admin_user, admin_pass)
    add_product(page, random_product)
    delete_product(page, random_product)

def test_homepage_loads(page: Page):
    page.goto(BASE_URL, wait_until="networkidle")
    expect(page.get_by_text("Nackademin Course App")).to_be_visible()