from playwright.sync_api import sync_playwright, expect

def test_negative_authorization():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        username_input = page.get_by_test_id('username')
        password_input = page.get_by_test_id('password')
        login_button = page.get_by_test_id('login-button')
        allert_text = page.get_by_test_id('error')

    def check_visible():
        expect(username_input).to_be_visible()
        expect(password_input).to_be_visible()
        expect(login_button).to_be_visible()

    def fill_login_form():
        username_input.fill('test_username')
        password_input.fill('password')

    def click_login_button():
        login_button.click()

    def check_visible_allert():
        expect(allert_text).to_have_value('Epic sadface: Username and password do not match any user in this service')
