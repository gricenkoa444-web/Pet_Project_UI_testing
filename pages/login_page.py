from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input = page.get_by_placeholder('username')
        self.password_input = page.get_by_placeholder('password')
        self.login_button = page.get_by_role("button", name="Login")
        self.alert_text = page.locator('.error-message-container.error [data-test="error"]')

    def fill_login_form(self, username: str, password: str):
        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_button(self):
        self.login_button.click()

    def check_visible_wrong_email_or_password_alert(self):
        expect(self.alert_text).to_have_text('Epic sadface: Username and password do not match any user in this service')

