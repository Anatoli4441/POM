import allure
from pages.customer_account_create import CustomerAccountCreatePage
from utils.randomizer import generate_random_first_name, generate_random_last_name, generate_random_email, \
    generate_random_password
from pages.locators.create_account_locators import CreateAccountLocators as Loc


@allure.feature('Customer Account Creation')
def test_correct_creation(page):
    create_page = CustomerAccountCreatePage(page)
    create_page.open()
    first_name = generate_random_first_name()
    last_name = generate_random_last_name()
    email = generate_random_email()
    password = generate_random_password()
    create_page.fill_create_form(first_name, last_name, email, password, password)
    create_page.create_account()
    create_page.verify_account_creation_success()


@allure.feature('Customer Account Creation')
def test_creation_with_all_empty_fields(page):
    create_page = CustomerAccountCreatePage(page)
    create_page.open()
    create_page.refresh_page()
    create_page.fill_create_form('', '', '', '', '')
    create_page.create_account()
    create_page.verify_field_error_message(Loc.FIRST_NAME_ERROR, "This is a required field.")
    create_page.verify_field_error_message(Loc.LAST_NAME_ERROR, "This is a required field.")
    create_page.verify_field_error_message(Loc.EMAIL_ERROR, "This is a required field.")
    create_page.verify_field_error_message(Loc.PASSWORD_ERROR, "This is a required field.")
    create_page.verify_field_error_message(Loc.CONFIRM_PASSWORD_ERROR, "This is a required field.")


@allure.feature('Customer Account Creation')
def test_different_values_in_password_and_confirm_password(page):
    create_page = CustomerAccountCreatePage(page)
    create_page.open()
    first_name = generate_random_first_name()
    last_name = generate_random_last_name()
    email = generate_random_email()
    password = generate_random_password()
    wrong_password = generate_random_password()
    create_page.fill_create_form(first_name, last_name, email, password, wrong_password)
    create_page.create_account()
    create_page.verify_field_error_message(Loc.CONFIRM_PASSWORD_ERROR, "Please enter the same value again.")
