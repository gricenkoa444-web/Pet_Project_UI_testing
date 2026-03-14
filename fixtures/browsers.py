from typing import Any, Generator

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import sync_playwright, \
    Page, Playwright

from pages.login_page import LoginPage
from config import settings
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture
def chromium_page() -> Generator[Page, Any, None]:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()

@pytest.fixture(scope='session')
def initialization_browse_state(playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page=page)
        login_page.visit('https://www.saucedemo.com/')
        login_page.fill_login_form(
            username=settings.test_user_username, password=settings.test_user_password
        )
        login_page.click_button()

        context.storage_state(path=settings.browser_state_file)
        browser.close()

@pytest.fixture(params=settings.browsers)
def chromium_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        storage_state=settings.browser_state_file
    )



