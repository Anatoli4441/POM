def assert_selected_option(expected, actual):
    assert actual.strip() == expected, f"The selected sorter option should be '{expected}'."


def assert_sorted_by_price(product_prices):
    assert product_prices == sorted(product_prices), "Products should be sorted by price in ascending order."


def assert_yes_filter_present(is_present):
    assert is_present, "The 'Yes' filter option should be present after selecting 'Eco Collection'."


def assert_account_created_successfully(is_created):
    assert is_created, "Account creation should be successful."


def assert_field_error_message(field_name, actual_message, expected_message="This is a required field."):
    assert actual_message == expected_message, f"Error message for {field_name} should be displayed."


def assert_password_mismatch_error(actual_message):
    expected_message = "Please enter the same value again."
    assert actual_message == expected_message, "Error message should indicate password mismatch."


def assert_mens_deals_present(is_present):
    assert is_present, "Men's Deals section should be present on the sale page."


def assert_gear_deals_present(is_present):
    assert is_present, "Gear Deals section should be present on the sale page."


def assert_correct_url(actual_url, expected_url):
    assert actual_url == expected_url, f"Expected URL to be {expected_url} but got {actual_url}"
