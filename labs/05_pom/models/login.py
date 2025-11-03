import re
from playwright.sync_api import expect

BASE_URL = "http://localhost:5173/"

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def goto(self):
        self.page.goto(BASE_URL, wait_until="networkidle")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()