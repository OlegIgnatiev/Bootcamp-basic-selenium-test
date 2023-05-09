from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class BasePage:

    class __WebDriver:

        def __init__(self):
            self.driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
            self.driver.implicitly_wait(5)

    driver = None

    def __init__(self):
        if not self.driver:
            BasePage.driver = BasePage.__WebDriver().driver

    def get_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def fill(self, by_locator, value):
        self.driver.find_element(*by_locator).send_keys(value)

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def clear(self, by_locator):
        self.driver.find_element(*by_locator).clear()

    def quite_driver(self):
        self.driver.quit()

    def open_url(self, url):
        self.driver.get(url)



