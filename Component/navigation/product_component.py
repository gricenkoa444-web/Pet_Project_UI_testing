from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from component.navigation.product_list_page_component import ProductListPageComponent
import re

class ProductComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sauce_labs_backpack = ProductListPageComponent(page, 'sauce-labs-backpack')
        self.sauce_labs_bike_light = ProductListPageComponent(page, 'sauce-labs-bike-light')
