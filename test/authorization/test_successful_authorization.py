import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    'username, password',
    [
        ('standard_user', 'secret_sauce'),
        ('locked_out_user', 'secret_sauce'),
        ('problem_user', 'secret_sauce'),
        ('performance_glitch_user', 'secret_sauce'),
        ('error_user', 'secret_sauce'),
        ('visual_user', 'secret_sauce'),

    ])
def test_successful_authorization(chromium_page: Page, username: str, password: str):
    login_page = LoginPage(chromium_page)
    login_page.visit('https://www.saucedemo.com/')
    login_page.fill_login_form(username=username, password=password)
    login_page.click_button()

    assert login_page.page.url == 'https://www.saucedemo.com/inventory.html'














