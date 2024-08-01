import pytest


@pytest.mark.regression
def test_sorter_default_option(collections_page):
    selected_option = collections_page.get_selected_sort_option()
    collections_page.assert_text(selected_option, "Position")


@pytest.mark.regression
def test_sort_by_price(collections_page):
    collections_page.open_page()
    collections_page.select_price_option()
    selected_option = collections_page.get_selected_sort_option()
    collections_page.assert_text(selected_option, "Price")

    product_prices = collections_page.get_product_prices()
    assert product_prices == sorted(product_prices), "Products should be sorted by price in ascending order."


@pytest.mark.regression
def test_sort_by_product_name(collections_page):
    collections_page.open_page()
    collections_page.select_product_name_option()
    selected_option = collections_page.get_selected_sort_option()
    collections_page.assert_text(selected_option, "Product Name")


@pytest.mark.regression
def test_eco_collection_value(collections_page):
    collections_page.open_page()
    collections_page.click_eco_collection()
    collections_page.is_yes_filter_present()
