from asyncio import wait_for

from playwright.sync_api import sync_playwright, expect

def test_successful_authorization():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        username_input = page.get_by_test_id('username')
        password_input = page.get_by_test_id('password')
        login_button = page.get_by_test_id('login-button')


    def check_visible():
        expect(username_input).to_be_visible()
        expect(password_input).to_be_visible()
        expect(login_button).to_be_visible()

    def fill_login_form():
        username_input.fill('standard_user')
        password_input.fill('secret_sauce')

    def click_login_button():
        login_button.click()













