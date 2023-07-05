from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class BasePage:

    class __WebDriver:
        def __init__(self):
            self.driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

    driver = None

    def __init__(self):
        if not self.driver:
            BasePage.driver = BasePage.__WebDriver().driver
        self.explicitly_wait = WebDriverWait(
            driver=self.driver,
            timeout=5
        )

    def get_url(self, url):
        self.driver.get("https://dev.bullphishid.net/login")

    def __is_element_present(self, by_locator) -> None:
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' element doesnt appear on the page")

    def __is_element_clickable(self, by_locator) -> None:
        self.explicitly_wait.until(expected_conditions.element_to_be_clickable(by_locator),
                                   message=f"'{by_locator}' element doesnt appear on the page")

    def if_element_not_present_on_the_page(self, by_locator) -> bool:
        try:
            self.__is_element_present(by_locator)
        except TimeoutException:
            if_element_presented = False
            return if_element_presented

    def get_element(self, by_locator):
        self.__is_element_present(by_locator)
        return self.driver.find_element(*by_locator)

    def fill(self, by_locator, value):
        self.__is_element_present(by_locator)
        self.driver.find_element(*by_locator).send_keys(value)

    def click(self, by_locator):
        self.__is_element_clickable(by_locator)
        self.driver.find_element(*by_locator).click()

    def clear(self, by_locator):
        self.__is_element_present(by_locator)
        self.driver.find_element(*by_locator).clear()

    def quite_driver(self):
        self.driver.quit()


