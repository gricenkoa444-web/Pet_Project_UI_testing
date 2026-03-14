from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.product_title = page.locator('[data-test="title"]')

        self.sauce_labs_backpack_title = page.locator('[data-test="inventory-item-name"]')
        self.sauce_labs_backpack_description = page.locator('[data-test="inventory-item-desc"]')
        self.sauce_labs_backpack_price = page.locator('[data-test="inventory-item-price"]').filter(has_text="$29.99")
        self.sauce_labs_backpack_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')

        self.sauce_labs_bike_light_title = page.locator('[data-test="inventory-item-name"]')
        self.sauce_labs_bike_light_description = page.locator('[data-test="inventory-item-desc"]')
        self.sauce_labs_bike_light_price = page.locator('[data-test="inventory-item-price"]')
        self.sauce_labs_bike_light_button = page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]')

        self.sauce_labs_bolt_tshirt_title = page.locator('[data-test="inventory-item-name"]')
        self.sauce_labs_bolt_tshirt_description = page.locator('[data-test="inventory-item-desc"]')
        self.sauce_labs_bolt_tshirt_price = page.locator('[data-test="inventory-item-price"]')
        self.sauce_labs_bolt_tshirt_button = page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')

        self.sauce_labs_fleece_jacket_title = page.locator('[data-test="inventory-item-name"]')
        self.sauce_labs_fleece_jacket_description = page.locator('[data-test="inventory-item-desc"]')
        self.sauce_labs_fleece_jacket_price = page.locator('[data-test="inventory-item-price"]')
        self.sauce_labs_fleece_jacket_button = page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]')

        self.sauce_labs_onesie_title = page.locator('[data-test="inventory-item-name"]')
        self.sauce_labs_onesie_description = page.locator('[data-test="inventory-item-desc"]')
        self.sauce_labs_onesie_price = page.locator('[data-test="inventory-item-price"]')
        self.sauce_labs_onesie_button = page.locator('[data-test="add-to-cart-sauce-labs-onesie"]')

        self.test_allthethings_tshirt_red_title = page.locator('[data-test="inventory-item-name"]')
        self.test_allthethings_tshirt_red_description = page.locator('[data-test="inventory-item-desc"]')
        self.test_allthethings_tshirt_red_price = page.locator('[data-test="inventory-item-price"]')
        self.test_allthethings_tshirt_red_button = page.locator(
            '[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]'
        )

    def check_visible_product_title(self):
        expect(self.product_title).to_be_visible()
        expect(self.product_title).to_have_text('Products')

    def check_visible_sauce_labs_backpack(self):
        expect(self.sauce_labs_backpack_title).to_be_visible()
        expect(self.sauce_labs_backpack_title).to_have_text('Sauce Labs Backpack')

        expect(self.sauce_labs_backpack_description).to_be_visible()
        expect(self.sauce_labs_backpack_description).to_have_text(
            'carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled '
            'laptop and tablet protection.'
        )

        expect(self.sauce_labs_backpack_price).to_be_visible()
        expect(self.sauce_labs_backpack_price).to_have_text("$29.99")

        expect(self.sauce_labs_backpack_button).to_be_visible()
        expect(self.sauce_labs_backpack_button).to_have_text('Add to cart')





