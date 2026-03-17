from playwright.sync_api import Page, expect
from Component.base_component import BaseComponent

class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_logo = page.locator('[data-test="primary-header"].header_label')
        self.shopping_cart_container = page.locator('data-test="shopping-cart-link"')
        self.open_button = page.get_by_role('button', name='react-burger-menu-btn')

    def check_visible(self):
        expect(self.open_button).to_be_visible()

        expect(self.app_logo).to_be_visible()
        expect(self.app_logo).to_have_text('Swag Labs')

        expect(self.shopping_cart_container).to_be_мшышиду()


