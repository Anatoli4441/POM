import allure


@allure.feature('Collections Page')
def test_sorter_default_option(collections_page):
    selected_option = collections_page.get_selected_sort_option()
    assert selected_option == "Position", f"Expected 'Position' but got '{selected_option}'"


@allure.feature('Collections Page')
def test_sort_by_price(collections_page):
    collections_page.open()
    collections_page.select_price_option()
    selected_option = collections_page.get_selected_sort_option()
    assert selected_option == "Price", f"Expected 'Price' but got '{selected_option}'"

    product_prices = collections_page.get_product_prices()
    sorted_prices = sorted(product_prices)
    assert product_prices == sorted_prices, "Products should be sorted by price in ascending order."


@allure.feature('Collections Page')
def test_sort_by_product_name(collections_page):
    collections_page.open()
    collections_page.select_product_name_option()
    selected_option = collections_page.get_selected_sort_option()
    assert selected_option == "Product Name", f"Expected 'Product Name' but got '{selected_option}'"


@allure.feature('Collections Page')
def test_eco_collection_value(collections_page):
    collections_page.open()
    collections_page.click_eco_collection()
    collections_page.is_yes_filter_present()
