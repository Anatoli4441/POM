import pytest
from pages.customer_account_create import CustomerAccountCreatePage
from pages.collections_page import CollectionsPage
from pages.sale_page import SalePage


@pytest.fixture()
def create_page(page):
    return CustomerAccountCreatePage(page)


@pytest.fixture()
def collections_page(page):
    return CollectionsPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
