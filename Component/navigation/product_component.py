from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from component.navigation.product_list_page_component import ProductListPageComponent
import re

class ProductComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sauce_labs_backpack = ProductListPageComponent(page, 'sauce-labs-backpack')

        self.sauce_labs_bike_light = ProductListPageComponent(page, 'sauce-labs-bike-light')

    def check_visible_sauce_labs_backpack(self):
        self.sauce_labs_backpack.check_visible(
            title="Sauce Labs Backpack",
            description='carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style '
                        'with unequaled laptop and tablet protection.',
            price=29.99
        )
    def check_visible_sauce_labs_bike_light(self):
        self.sauce_labs_backpack.check_visible(
            title="Sauce Labs Bike Light",
            description="A red light isn't the desired state in testing but it sure helps when riding your bike at "
                        "night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
            price=9.99
        )

    def click_button(self):
        self.sauce_labs_backpack.navigate()
