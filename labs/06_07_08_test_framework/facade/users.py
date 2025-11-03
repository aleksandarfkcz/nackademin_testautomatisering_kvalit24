class UsersFacade:
    def init(self, page):
        self.page = page

    def login_as_new_user(self):
        username = libs.utils.generate_string_with_prefix(prefix="user")
        password = "pass123"
        home = HomePage(self.page)
        home.navigate()
        home.go_to_signup()
        signup = SignupPage(self.page)
        signup.signup(username, password)
        signup.go_to_home()
        home.login(username, password)
        return username, password 