from pages.base_page import BasePage
from pages.locators.create_locators import mens_deals_title_loc, gear_deals_title_loc, shop_womens_deals_button_loc, \
    shop_luma_gear_button_loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def is_mens_deals_present(self):
        self.assert_element_visible(mens_deals_title_loc)

    def is_gear_deals_present(self):
        self.assert_element_visible(gear_deals_title_loc)

    def click_shop_womens_deals(self):
        self.wait_for_element(shop_womens_deals_button_loc).click()

    def click_shop_luma_gear(self):
        self.wait_for_element(shop_luma_gear_button_loc).click()
