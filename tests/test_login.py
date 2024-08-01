import pytest
from utils.randomizer import generate_random_first_name, generate_random_last_name, generate_random_email, \
    generate_random_password


@pytest.mark.smoke
def test_correct_creation(create_page):
    first_name = generate_random_first_name()
    last_name = generate_random_last_name()
    email = generate_random_email()
    password = generate_random_password()
    create_page.refresh_page()
    create_page.fill_create_form(first_name, last_name, email, password, password)
    create_page.create_account()
    create_page.is_account_created_successfully()


@pytest.mark.smoke
def test_creation_with_all_empty_fields(create_page):
    create_page.refresh_page()
    create_page.fill_create_form('', '', '', '', '')
    create_page.create_account()

    first_name_error = create_page.get_field_error_message("firstname")
    last_name_error = create_page.get_field_error_message("lastname")
    email_error = create_page.get_field_error_message("email_address")
    password_error = create_page.get_field_error_message("password")
    confirm_password_error = create_page.get_field_error_message("password-confirmation")

    assert first_name_error == "This is a required field."
    assert last_name_error == "This is a required field."
    assert email_error == "This is a required field."
    assert password_error == "This is a required field."
    assert confirm_password_error == "This is a required field."


@pytest.mark.smoke
def test_different_values_in_password_and_confirm_password(create_page):
    first_name = generate_random_first_name()
    last_name = generate_random_last_name()
    email = generate_random_email()
    password = generate_random_password()
    wrong_password = generate_random_password()

    create_page.refresh_page()
    create_page.fill_create_form(first_name, last_name, email, password, wrong_password)
    create_page.create_account()
    error_message = create_page.get_confirm_password_error_message()
    assert error_message == "Please enter the same value again."
