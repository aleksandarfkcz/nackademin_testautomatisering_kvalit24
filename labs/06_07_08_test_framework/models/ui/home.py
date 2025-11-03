import os 

class HomePage:
    def __init__(self, page):
        self.page = page
        self.login_header_main_title = page.get_by_text('Nackademin Course App')
        self.login_input_username = page.get_by_placeholder('Username')
        self.login_input_password = page.get_by_placeholder('Password')
        self.login_btn_login = page.locator('button.button-primary')
        self.login_label_have_account = page.get_by_text("Don't have an account?")
        self.login_btn_signup = page.locator('#signup')

        self._base_url = (
            os.getenv("FRONTEND_URL")
            or os.getenv("APP_FRONT_URL")
            or "http://localhost:5173/"
        ).rstrip("/")

    def navigate(self):
        self.page.goto(self._base_url + "/")

    def login(self,username,password):
        self.login_input_username.fill(username)
        self.login_input_password.fill(password)
        self.login_btn_login.click()

    def go_to_signup(self):
        # Click the Sign Up button
        self.login_btn_signup.click()
        self.page.get_by_role("button", name="Login").wait_for(state="visible")