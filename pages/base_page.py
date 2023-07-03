from selenium import webdriver
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

    def get_element(self, by_locator):
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' element doesnt appear on the page")
        return self.driver.find_element(*by_locator)

    def fill(self, by_locator, value):
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' element doesnt appear on the page")
        self.driver.find_element(*by_locator).send_keys(value)

    def click(self, by_locator):
        self.explicitly_wait.until(expected_conditions.element_to_be_clickable(by_locator),
                                   message=f"'{by_locator}' element doesnt appear on the page")
        self.driver.find_element(*by_locator).click()

    def clear(self, by_locator):
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator),
                                   message=f"'{by_locator}' element doesnt appear on the page")
        self.driver.find_element(*by_locator).clear()

    def clear_fill_click(self, by_locator_field_username, value_username, by_locator_field_password, value_password, by_locator_button):
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator_field_username),
                                   message=f"'{by_locator_field_username}' element doesnt appear on the page")
        self.driver.find_element(*by_locator_field_username).clear()
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator_field_username),
                                   message=f"'{by_locator_field_username}' element doesnt appear on the page")
        self.driver.find_element(*by_locator_field_username).send_keys(value_username)

        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator_field_password),
                                   message=f"'{by_locator_field_password}' element doesnt appear on the page")
        self.driver.find_element(*by_locator_field_password).clear()
        self.explicitly_wait.until(expected_conditions.presence_of_element_located(by_locator_field_password),
                                   message=f"'{by_locator_field_password}' element doesnt appear on the page")
        self.driver.find_element(*by_locator_field_password).send_keys(value_password)

        self.explicitly_wait.until(expected_conditions.element_to_be_clickable(by_locator_button),
                                   message=f"'{by_locator_button}' element doesnt appear on the page")
        self.driver.find_element(*by_locator_button).click()

    def quite_driver(self):
        self.driver.quit()


