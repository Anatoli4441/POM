from playwright.sync_api import Page
import allure


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open the page')
    def open(self):  # Renamed to open
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page URL is not provided')

    @allure.step('Refresh the page')
    def refresh_page(self):
        self.page.reload()

    @allure.step('Find element by locator')
    def find(self, locator: str):
        return self.page.locator(locator)

    @allure.step('Assert element visibility')
    def assert_element_visible(self, locator: str):
        self.page.wait_for_selector(locator, state='visible')
        assert self.page.locator(locator).is_visible()

    @allure.step('Assert URL')
    def assert_url(self, expected_url: str):
        assert self.page.url == expected_url, f"Expected URL '{expected_url}', but got '{self.page.url}'"

    @allure.step('Assert text')
    def assert_text(self, actual_text: str, expected_text: str):
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
