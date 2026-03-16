from playwright.sync_api import sync_playwright, expect, Page
import pytest
from pages.login_page import LoginPage
@pytest.mark.xdist_group(name="authorization")
@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    'username,password',
    [
        ('test', 'password')
    ]
)
def test_negative_authorization(chromium_page: Page, username: str, password: str):
    login_page = LoginPage(chromium_page)
    login_page.visit('https://www.saucedemo.com/')
    login_page.fill_login_form(username=username, password=password)
    login_page.click_button()
    login_page.check_visible_wrong_email_or_password_alert()
