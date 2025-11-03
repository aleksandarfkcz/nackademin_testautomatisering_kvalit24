import re
import time
from playwright.sync_api import Page
from models.login import LoginPage
from models.home import HomePage

BASE_URL = "http://localhost:5173/"
admin_user = "admin"
admin_pass = "123456789"
random_product = f"prod_{int(time.time())}"

# Control that page loading correctly 
def test_homepage_loads(page: Page):
    page.goto(BASE_URL, wait_until="networkidle")
    home = HomePage(page)
    home.verify_homepage_loaded()



# Log in as a admin
def test_admin_can_add_and_delete(page: Page):
    login = LoginPage(page)
    login.goto()
    login.login(admin_user, admin_pass)

    home = HomePage(page)
    home.add_product(random_product)
    home.delete_product(random_product)