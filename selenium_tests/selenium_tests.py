import time
import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestSelenium(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)

    def test_login_validation(self):
        self.driver.get(url="https://dev.bullphishid.net/login")
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').send_keys("emaildomain.com")
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-password-input"]').send_keys("123456789")
        self.driver.find_element(By.XPATH, '//button[text()="Log In"]').click()

        self.assertTrue(self.driver.find_element(By.XPATH, '//div[text()="The email must be a valid email address."]'))

        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').clear()
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').send_keys("oleh.admin@email.com")
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-password-input"]').clear()
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-password-input"]').send_keys("123456789")
        self.driver.find_element(By.XPATH, '//button[text()="Log In"]').click()

        self.assertTrue(self.driver.find_element(By.XPATH, '//div[contains(text() , "Please check your credentials")]'))

        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').clear()
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').send_keys("email@domain.com")
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-password-input"]').clear()
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-password-input"]').send_keys("Olegignatiev1!")
        self.driver.find_element(By.XPATH, '//button[text()="Log In"]').click()

        self.assertTrue(self.driver.find_element(By.XPATH, '//div[contains(text() , "Please check your credentials")]'))

        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').clear()
        self.driver.find_element(By.XPATH, '//input[@data-testid="login-form-username-input"]').send_keys("Oleh.admin@email.com")
        self.driver.find_element(By.XPATH, '//button[text()="Log In"]').click()

        if_element_is_present = True
        try:
            self.driver.find_element(By.XPATH, '//button[text()="Log In"]')
        except NoSuchElementException:
            if_element_is_present = False
        self.assertFalse(if_element_is_present)

        self.driver.find_element(By.XPATH, '//input[@id ="code"]').send_keys("123456789")
        self.driver.find_element(By.XPATH, '//button[text() ="Verify"]').click()

        self.assertTrue(self.driver.find_element(By.XPATH, '//div[text() ="The authentication code must be 6 digits."]'))

        self.driver.find_element(By.XPATH, '//input[@id ="code"]').clear()
        self.driver.find_element(By.XPATH, '//input[@id ="code"]').send_keys("000000")
        self.driver.find_element(By.XPATH, '//button[text() ="Verify"]').click()

        self.assertTrue(self.driver.find_element(By.XPATH, '//div[text() ="Invalid authentication code, please try again"]'))

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
