import pytest


@pytest.mark.extended
def test_mens_deals_present(sale_page):
    sale_page.open_page()
    sale_page.is_mens_deals_present()


@pytest.mark.extended
def test_gear_deals_present(sale_page):
    sale_page.open_page()
    sale_page.is_gear_deals_present()


@pytest.mark.extended
def test_click_shop_womens_deals(sale_page):
    sale_page.open_page()
    sale_page.click_shop_womens_deals()
    sale_page.assert_url("https://magento.softwaretestingboard.com/promotions/women-sale.html")


@pytest.mark.extended
def test_click_shop_luma_gear(sale_page):
    sale_page.open_page()
    sale_page.click_shop_luma_gear()
    sale_page.assert_url("https://magento.softwaretestingboard.com/gear.html")
