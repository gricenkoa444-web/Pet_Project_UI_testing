from playwright.sync_api import sync_playwright, expect, Page
from pages.products_page import ProductPage

def test_dashboard_product(chromium_page_with_state: Page):
    product_page = ProductPage(chromium_page_with_state)
    product_page.visit('https://www.saucedemo.com/inventory.html')
    product_page.check_visible_product_title()
    product_page.check_visible_sauce_labs_backpack()







