from pages.base_page import BasePage
from pages.locators.create_account_locators import CreateAccountLocators as Loc
import allure


class CustomerAccountCreatePage(BasePage):
    page_url = '/customer/account/create'

    @allure.step('Fill the account creation form')
    def fill_create_form(self, first_name, last_name, email, password, confirm_password):
        self.page.locator(Loc.FIRST_NAME).fill(first_name)
        self.page.locator(Loc.LAST_NAME).fill(last_name)
        self.page.locator(Loc.EMAIL).fill(email)
        self.page.locator(Loc.PASSWORD).fill(password)
        self.page.locator(Loc.CONFIRM_PASSWORD).fill(confirm_password)

    @allure.step('Click create account button')
    def create_account(self):
        self.page.locator(Loc.CREATE_ACCOUNT_BUTTON).click()

    @allure.step('Check if account was created successfully')
    def is_account_created_successfully(self):
        self.assert_element_visible(Loc.SUCCESS_MESSAGE)

    @allure.step('Get field error message')
    def get_field_error_message(self, locator):
        return self.page.locator(locator).inner_text().strip()
