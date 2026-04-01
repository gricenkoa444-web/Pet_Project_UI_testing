from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from typing import Pattern

class ProductListPageComponent(BaseComponent):
    def __init__(self, page:Page, identifier: str):
        super().__init__(page)

        self.name_item = page.locator(f'data-test="inventory-item-{identifier}"')
        self.description_item = page.locator(f'data-test="inventory-item-{identifier}"')
        self.price_item = page.locator(f'data-test="inventory-item-{identifier}"')
        self.add_card_item = page.locator(f'data-test="add-to-cart-{identifier}"')

    def check_visible(self, title: str, description: str, price: float):
        expect(self.name_item).to_be_visible()
        expect(self.name_item).to_have_text(title)

        expect(self.description_item).to_be_visible()
        expect(self.description_item).to_have_text(description)

        expect(self.price_item).to_be_visible()
        expect(self.price_item).to_have_text(price)

        expect(self.add_card_item).to_be_visible()
        expect(self.add_card_item).to_have_text(title)

    def navigate(self, expected_url: Pattern[str]):
        self.add_card_item.click()
        self.check_current_url(expected_url)