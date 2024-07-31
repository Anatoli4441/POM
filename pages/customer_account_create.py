from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
from pages.locators.create_locators import (
    confirm_password_error_loc,
    success_message_loc,
    create_account_button_loc,
    confirm_password_loc,
    password_loc,
    first_name_loc,
    last_name_loc,
    email_loc
)


class CustomerAccountCreate(BasePage):
    page_url = '/customer/account/create'

    def fill_create_form(self, first_name, last_name, email, password, confirm_password):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(first_name_loc)
        ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(last_name_loc)
        ).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(email_loc)
        ).send_keys(email)
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(password_loc)
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(confirm_password_loc)
        ).send_keys(confirm_password)

    def create_account(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(create_account_button_loc)
        ).click()

    def is_account_created_successfully(self):
        try:
            success_element = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(success_message_loc)
            )
            return success_element.is_displayed()
        except TimeoutException:
            return False

    def get_field_error_message(self, field_id):
        error_locator = (By.ID, f"{field_id}-error")
        try:
            error_message_element = WebDriverWait(self.driver, 15).until(
                ec.visibility_of_element_located(error_locator)
            )
            return error_message_element.text
        except TimeoutException:
            return None

    def get_confirm_password_error_message(self):
        try:
            error_element = WebDriverWait(self.driver, 15).until(
                ec.visibility_of_element_located(confirm_password_error_loc)
            )
            return error_element.text
        except TimeoutException:
            return None

    def refresh_page(self):
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(first_name_loc)
        )
