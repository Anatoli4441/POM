from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
from pages.locators import create_locators


class CollectionsPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def open_page(self):
        self.driver.get(f"{self.base_url}{self.page_url}")

    def get_selected_sort_option(self):
        try:
            sorter_element = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(create_locators.sorter_select_loc)
            )
            select = Select(sorter_element)
            return select.first_selected_option.text
        except NoSuchElementException:
            return None

    def select_price_option(self):
        try:
            sorter_element = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable(create_locators.sorter_select_loc)
            )
            select = Select(sorter_element)
            select.select_by_visible_text('Price')
        except NoSuchElementException:
            print("Sorter select element not found or clickable.")

    def select_product_name_option(self):
        try:
            sorter_element = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable(create_locators.sorter_select_loc)
            )
            select = Select(sorter_element)
            select.select_by_visible_text('Product Name')
        except NoSuchElementException:
            print("Sorter select element not found or clickable.")

    def get_product_prices(self):
        try:
            price_elements = WebDriverWait(self.driver, 10).until(
                ec.presence_of_all_elements_located(create_locators.price_loc)
            )
            return [float(price.text.replace('$', '').replace(',', '').strip()) for price in price_elements if
                    price.text]
        except NoSuchElementException:
            return []

    def click_eco_collection(self):
        try:
            eco_collection_element = WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable(create_locators.eco_collection_filter_loc)
            )
            eco_collection_element.click()
        except NoSuchElementException:
            print("Eco collection filter element not found or clickable.")

    def is_yes_filter_present(self):
        try:
            WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(create_locators.yes_filter_option_loc)
            )
            return True
        except NoSuchElementException:
            return False
