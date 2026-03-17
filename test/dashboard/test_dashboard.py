from playwright.sync_api import sync_playwright, expect, Page

from config import settings
from pages.products_page import ProductPage
import pytest
#@pytest.mark.regression
def test_dashboard_product(chromium_page_with_state: Page):
    product_page = ProductPage(chromium_page_with_state)

    base_url = str(settings.app_url)
    product_page.visit(f"{base_url}/inventory.html")

    product_page.visit('https://www.saucedemo.com/inventory.html')
    product_page.check_visible_product_title()
    product_page.check_visible_all_products()







