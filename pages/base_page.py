from behave.runner import Context
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, context: Context):
        self.driver = context.driver
        self.explicitly_wait = WebDriverWait(
            driver=self.driver,
            timeout=5
        )

    def get_url(self, url):
        """
        Get URL of project.
        """
        self.driver.get("https://dev.bullphishid.net/login")

    def __is_element_present(self, by_locator: tuple[By, str]) -> None:
        """
        Check that element is present on the page.
        """
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' element doesnt appear on the page")

    def __is_element_not_presented(self, by_locator: tuple[By, str]) -> None:
        """
        Check that element is not present on the page.
        """
        self.explicitly_wait.until(expected_conditions.invisibility_of_element_located(by_locator),
                                   message=f"'{by_locator}' element is presented on the page, but it should not")

    def __is_element_clickable(self, by_locator: tuple[By, str]) -> None:
        """
        Check that element on the page is clickable.
        """
        self.explicitly_wait.until(expected_conditions.element_to_be_clickable(by_locator),
                                   message=f"'{by_locator}' element doesnt appear on the page")

    def if_element_displayed(self, by_locator: tuple[By, str]):
        self.__is_element_present(by_locator)
        return True

    def if_element_not_present_on_the_page(self, by_locator: tuple[By, str]) -> bool:
        """
        Check that elements is not present on the page and avoid TimeoutException.
        """
        self.__is_element_not_presented(by_locator)
        return True

    def fill(self, by_locator: tuple[By, str], value: str):
        """
        Fill the element by locator.
        """
        self.__is_element_present(by_locator)
        self.driver.find_element(*by_locator).send_keys(value)

    def click(self, by_locator: tuple[By, str]):
        """
        Click the element by locator.
        """
        self.__is_element_clickable(by_locator)
        self.driver.find_element(*by_locator).click()

    def clear(self, by_locator: tuple[By, str]):
        """
        Clear the element by locator.
        """
        self.__is_element_present(by_locator)
        self.driver.find_element(*by_locator).clear()

    def refresh_page(self) -> None:
        """
        Refresh page
        """
        self.driver.refresh()

    def clear_cookies(self) -> None:
        """
        Clear cookies and then refresh page
        """
        self.driver.delete_all_cookies()
        self.refresh_page()

    def quite_driver(self):
        self.driver.quit()





