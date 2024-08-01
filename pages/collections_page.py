from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from pages.locators.create_locators import sorter_select_loc, price_loc, eco_collection_filter_loc, \
    yes_filter_option_loc


class CollectionsPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def get_selected_sort_option(self):
        sorter = self.wait_for_element(sorter_select_loc)
        return Select(sorter).first_selected_option.text

    def select_price_option(self):
        sorter = self.wait_for_element(sorter_select_loc)
        Select(sorter).select_by_value('price')

    def select_product_name_option(self):
        sorter = self.wait_for_element(sorter_select_loc)
        Select(sorter).select_by_value('name')

    def get_product_prices(self):
        prices = self.find_all(price_loc)
        return [float(price.text[1:]) for price in prices if price.text]

    def click_eco_collection(self):
        self.wait_for_element(eco_collection_filter_loc).click()

    def is_yes_filter_present(self):
        self.assert_element_visible(yes_filter_option_loc)
