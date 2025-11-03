class SignupPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.signup_button = page.get_by_role("button", name="Signup")

    def signup(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.signup_button.click()