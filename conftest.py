from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.customer_account_create import CustomerAccountCreate
from pages.collections_page import CollectionsPage
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def create_page(driver):
    page = CustomerAccountCreate(driver)
    page.open_page()
    return page


@pytest.fixture()
def collections_page(driver):
    page = CollectionsPage(driver)
    page.open_page()
    return page


@pytest.fixture()
def sale_page(driver):
    page = SalePage(driver)
    page.open_page()
    return page
