from pages.base_page import BasePage
from pages.locators.collections_page_locators import CollectionsPageLocators as Loc
import allure


class CollectionsPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    @allure.step('Get selected sort option')
    def get_selected_sort_option(self):
        selected_option = self.page.locator("select.sorter-options option:checked").first.inner_text().strip()
        return selected_option

    @allure.step('Select price option')
    def select_price_option(self):
        # Используем уточнение локатора для выбора первого элемента
        self.page.locator('select.sorter-options').nth(0).select_option('price')

    @allure.step('Select product name option')
    def select_product_name_option(self):
        # Используем уточнение локатора для выбора первого элемента
        self.page.locator('select.sorter-options').nth(0).select_option('name')

    @allure.step('Get product prices')
    def get_product_prices(self):
        prices_elements = self.page.locator(Loc.PRICE_LOC).all()
        prices = []
        for price_element in prices_elements:
            if price_element.is_visible():
                price_text = price_element.inner_text().strip().replace('$', '')
                try:
                    price = float(price_text)
                    prices.append(price)
                except ValueError:
                    continue
        return prices

    @allure.step('Click on eco collection')
    def click_eco_collection(self):
        self.page.locator(Loc.ECO_COLLECTION_FILTER).click()

    @allure.step('Check if yes filter is present')
    def is_yes_filter_present(self):
        self.assert_element_visible(Loc.YES_FILTER_OPTION)
