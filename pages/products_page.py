from playwright.sync_api import Page, expect

from Component.navigation.navbar_component import NavbarComponent
from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page: Page, dentifier: str):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.product_title = page.locator('[data-test="title"]')

        self.sauce_labs_backpack_title = page.locator(f'[data-test="inventory-item-{dentifier}"]')
        self.sauce_labs_backpack_description = page.locator(f'[data-test="inventory-item-{dentifier}"]')
        self.sauce_labs_backpack_price = page.locator(f'[data-test="inventory-item-{dentifier}"]')

        self.sauce_labs_bike_light_button = page.locator(f'[data-test="add-to-cart-sauce-labs-{dentifier}"]')

    def check_visible_product_title(self, title: str):
        expect(self.product_title).to_be_visible()
        expect(self.product_title).to_have_text(title)

    def check_visible_all_products(self, title: str, description: str, price: float):
        expect(self.sauce_labs_backpack_title).to_be_visible()
        expect(self.sauce_labs_backpack_title).to_have_text(title)

        expect(self.sauce_labs_backpack_description).to_be_visible()
        expect(self.sauce_labs_backpack_description).to_have_text(description)

        expect(self.sauce_labs_backpack_price).to_be_visible()
        expect(self.sauce_labs_backpack_price).to_have_text(price)

        expect(self.sauce_labs_backpack_button).to_be_visible()
        expect(self.sauce_labs_backpack_button).to_have_text(title)





