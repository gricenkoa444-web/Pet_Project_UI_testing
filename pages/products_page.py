from playwright.sync_api import Page, expect

from component.navigation.navbar_component import NavbarComponent
from component.navigation.product_component import ProductComponent
from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.product_component = ProductComponent(page)











