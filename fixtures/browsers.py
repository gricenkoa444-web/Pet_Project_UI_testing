from typing import Any, Generator

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import sync_playwright, \
    Page, Playwright

from pages.login_page import LoginPage
from config import settings, Browser
from tools.playwright.pages import initialize_playwright_page


@pytest.fixture(params=settings.browser)
def chromium_page(request: SubRequest, playwright: Playwright) -> Generator[Page, Any, None]:
    with initialize_playwright_page(
            playwright,
            test_name=request.node.name,
            browser_type=request.param,
    ) as page:
        yield page


@pytest.fixture(scope='session')
def initialization_browse_state(
        playwright: Playwright,
        request,
        test_name: str,
        browser_type: Browser[0],
        storage_state: str | None = None,
):
        browser = playwright[browser_type].launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        login_page = LoginPage(page=page)
        login_page.visit('https://www.saucedemo.com/')
        login_page.fill_login_form(
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        login_page.click_button()

        context.storage_state(path=settings.browser_state_file)
        state_path = settings.browser_state_file
        print(f"Сохраняем состояние в: {state_path.absolute()}")
        print(f"Файл существует после сохранения? {state_path.exists()}")
        print(f"Размер файла: {state_path.stat().st_size if state_path.exists() else 0} байт")
        browser.close()

        return settings.browser_state_file

@pytest.fixture(params=settings.browser)
def chromium_page_with_state(initialization_browse_state, request: SubRequest, playwright: Playwright) -> Page:
    with initialize_playwright_page(
        playwright,
        browser_type=request.param,
        test_name=request.node.name,
        storage_state=settings.browser_state_file
    )as page:
        yield page



