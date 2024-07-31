import pytest

from utils.assert_helpers import assert_mens_deals_present, assert_gear_deals_present, assert_correct_url
from utils.urls import womens_deals_url, luma_url


@pytest.mark.extended
def test_mens_deals_present(sale_page):
    sale_page.open_page()
    is_present = sale_page.is_mens_deals_present()
    assert_mens_deals_present(is_present)


@pytest.mark.extended
def test_gear_deals_present(sale_page):
    sale_page.open_page()
    is_present = sale_page.is_gear_deals_present()
    assert_gear_deals_present(is_present)


@pytest.mark.extended
def test_click_shop_womens_deals(sale_page):
    sale_page.open_page()
    sale_page.click_shop_womens_deals()
    actual_url = sale_page.driver.current_url
    assert_correct_url(actual_url, womens_deals_url)


@pytest.mark.extended
def test_click_shop_luma_gear(sale_page):
    sale_page.open_page()
    sale_page.click_shop_luma_gear()
    actual_url = sale_page.driver.current_url
    assert_correct_url(actual_url, luma_url)
