from pages.base_page import BasePage
from pages.locators.sale_page_locators import SalePageLocators as Loc
import allure


class SalePage(BasePage):
    page_url = '/sale.html'

    @allure.step('Verify mens deals are present')
    def verify_mens_deals_present(self):
        self.assert_element_visible(Loc.MENS_DEALS_TITLE)

    @allure.step('Verify gear deals are present')
    def verify_gear_deals_present(self):
        self.assert_element_visible(Loc.GEAR_DEALS_TITLE)

    @allure.step('Click on shop women’s deals')
    def click_shop_womens_deals(self):
        self.find(Loc.SHOP_WOMENS_DEALS_BUTTON).click()

    @allure.step('Click on shop luma gear')
    def click_shop_luma_gear(self):
        self.find(Loc.SHOP_LUMA_GEAR_BUTTON).click()
