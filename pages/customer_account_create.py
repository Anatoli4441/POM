from pages.base_page import BasePage
from pages.locators.create_locators import first_name_loc, last_name_loc, \
    email_loc, password_loc, confirm_password_loc, \
    create_account_button_loc, success_message_loc, first_name_error_loc, \
    last_name_error_loc, email_error_loc, \
    password_error_loc, confirm_password_error_loc


class CustomerAccountCreate(BasePage):
    page_url = '/customer/account/create/'

    def fill_create_form(self, first_name, last_name, email, password, confirm_password):
        print("Filling the create account form")
        self.wait_for_element(first_name_loc).send_keys(first_name)
        self.wait_for_element(last_name_loc).send_keys(last_name)
        self.wait_for_element(email_loc).send_keys(email)
        self.wait_for_element(password_loc).send_keys(password)
        self.wait_for_element(confirm_password_loc).send_keys(confirm_password)

    def create_account(self):
        print("Creating account")
        self.wait_for_element(create_account_button_loc).click()

    def is_account_created_successfully(self):
        print("Checking if account was created successfully")
        self.assert_element_visible(success_message_loc)

    def get_field_error_message(self, field_name):
        print(f"Getting error message for field: {field_name}")
        locators = {
            "firstname": first_name_error_loc,
            "lastname": last_name_error_loc,
            "email_address": email_error_loc,
            "password": password_error_loc,
            "password-confirmation": confirm_password_error_loc
        }
        return self.wait_for_element(locators[field_name]).text

    def get_confirm_password_error_message(self):
        print("Getting confirm password error message")
        return self.wait_for_element(confirm_password_error_loc).text
