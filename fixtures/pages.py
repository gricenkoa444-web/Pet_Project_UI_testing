import pytest
from playwright.sync_api import Page

from pages.products_page import ProductPage


@pytest.fixture
def product_page_with_state(chromium_page_with_state: Page) -> ProductPage:
    return ProductPage(page=chromium_page_with_state)