import allure


@allure.feature('Collections Page')
def test_sorter_default_option(collections_page):
    collections_page.open()
    collections_page.verify_sort_option("Position")


@allure.feature('Collections Page')
def test_sort_by_price(collections_page):
    collections_page.open()
    collections_page.select_price_option()
    collections_page.verify_sort_option("Price")
    collections_page.verify_product_prices_sorted()


@allure.feature('Collections Page')
def test_sort_by_product_name(collections_page):
    collections_page.open()
    collections_page.select_product_name_option()
    collections_page.verify_sort_option("Product Name")


@allure.feature('Collections Page')
def test_eco_collection_value(collections_page):
    collections_page.open()
    collections_page.click_eco_collection()
    collections_page.verify_yes_filter_present()
