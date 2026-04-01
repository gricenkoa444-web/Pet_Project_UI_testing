from playwright.sync_api import sync_playwright, expect, Page

from config import settings
from pages.products_page import ProductPage
import pytest

@pytest.mark.regression
def test_dashboard_product(product_page_with_state: ProductPage):
    product_page_with_state.visit('https://www.saucedemo.com/inventory.html')
    product_page_with_state.navbar.check_visible()
    product_page_with_state.product_component.check_visible_sauce_labs_backpack()
    product_page_with_state.product_component.check_visible_sauce_labs_bike_light()
    product_page_with_state.product_component.click_button()








