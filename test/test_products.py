from playwright.sync_api import sync_playwright, expect

def test_products_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/inventory.html")

        title_products = page.get_by_test_id('title')

        inventory_item = page.get_by_test_id('inventory-item')
        inventory_image = page.get_by_test_id('item-0-title-link')
        item_description = page.get_by_test_id('inventory-item-description')
        item_name = page.get_by_test_id('inventory-item-name')
        item_description = page.get_by_test_id('inventory-item-desc')
        item_price = page.get_by_test_id('inventory-item-price')
        button_add = page.get_by_test_id('add-to-cart-sauce-labs-backpack')





