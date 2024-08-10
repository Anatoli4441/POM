import pytest
from pages.customer_account_create import CustomerAccountCreatePage
from pages.collections_page import CollectionsPage
from pages.sale_page import SalePage

@pytest.fixture()
def create_page(page):
    create_page = CustomerAccountCreatePage(page)
    create_page.open()
    return create_page

@pytest.fixture()
def collections_page(page):
    collections_page = CollectionsPage(page)
    collections_page.open()
    return collections_page

@pytest.fixture()
def sale_page(page):
    sale_page = SalePage(page)
    sale_page.open()
    return sale_page
