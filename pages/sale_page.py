from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from pages.base_page import BasePage
from pages.locators.create_locators import (
    mens_deals_title_loc,
    gear_deals_title_loc,
    shop_womens_deals_button_loc,
    shop_luma_gear_button_loc
)


class SalePage(BasePage):
    page_url = '/sale.html'

    def open_page(self):
        self.driver.get(f"{self.base_url}{self.page_url}")

    def is_mens_deals_present(self):
        try:
            mens_deals_locator = mens_deals_title_loc
            WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(mens_deals_locator)
            )
            return True
        except TimeoutException:
            print("Timeout: Mens's Deals section not found or not visible.")
            return False

    def is_gear_deals_present(self):
        try:
            gear_deals_locator = gear_deals_title_loc
            WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(gear_deals_locator)
            )
            return True
        except TimeoutException:
            print("Timeout: Gear Deals section not found or not visible.")
            return False

    def click_shop_womens_deals(self):
        try:
            shop_womens_deals_locator = shop_womens_deals_button_loc
            WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable(shop_womens_deals_locator)
            ).click()
        except TimeoutException:
            print("Timeout: Shop Women’s Deals button not found or not clickable.")
        except NoSuchElementException:
            print("Element not found: Shop Women’s Deals button.")
        except ElementClickInterceptedException:
            print("Click intercepted: Unable to click on Shop Women’s Deals button.")

    def click_shop_luma_gear(self):
        try:
            shop_luma_gear_locator = shop_luma_gear_button_loc
            WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable(shop_luma_gear_locator)
            ).click()
        except TimeoutException:
            print("Timeout: Shop Luma Gear button not found or not clickable.")
        except NoSuchElementException:
            print("Element not found: Shop Luma Gear button.")
        except ElementClickInterceptedException:
            print("Click intercepted: Unable to click on Shop Luma Gear button.")
