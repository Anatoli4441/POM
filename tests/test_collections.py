import pytest

from utils.assert_helpers import assert_selected_option, assert_sorted_by_price, assert_yes_filter_present


@pytest.mark.regression
def test_sorter_default_option(collections_page):
    selected_option = collections_page.get_selected_sort_option()
    assert_selected_option("Position", selected_option)


@pytest.mark.regression
def test_sort_by_price(collections_page):
    collections_page.open_page()
    collections_page.select_price_option()
    selected_option = collections_page.get_selected_sort_option()
    assert_selected_option("Price", selected_option)

    product_prices = collections_page.get_product_prices()
    assert_sorted_by_price(product_prices)


@pytest.mark.regression
def test_sort_by_product_name(collections_page):
    collections_page.open_page()
    collections_page.select_product_name_option()
    selected_option = collections_page.get_selected_sort_option()
    assert_selected_option("Product Name", selected_option)


@pytest.mark.regression
def test_eco_collection_value(collections_page):
    collections_page.open_page()
    collections_page.click_eco_collection()
    is_yes_filter_present = collections_page.is_yes_filter_present()
    assert_yes_filter_present(is_yes_filter_present)
