from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            print(f"Opening page: {self.base_url}{self.page_url}")
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for this page class')

    def refresh_page(self):
        print("Refreshing page")
        self.driver.refresh()

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def wait_for_element(self, locator: tuple):
        print(f"Waiting for element {locator} to be present")
        return WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(locator)
        )

    def wait_for_element_to_be_visible(self, locator: tuple):
        print(f"Waiting for element {locator} to be visible")
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(locator)
        )

    def assert_element_present(self, locator: tuple):
        element = self.wait_for_element_to_be_visible(locator)
        assert element.is_displayed(), f"Element {locator} not displayed."

    def assert_text(self, actual_text, expected_text):
        assert actual_text.strip() == expected_text, f"Expected text '{expected_text}', but got '{actual_text.strip()}'"

    def assert_url(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Expected URL to be '{expected_url}', but got '{actual_url}'"

    def assert_element_visible(self, locator: tuple):
        assert WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(locator)
        ).is_displayed(), f"Element {locator} is not visible."
