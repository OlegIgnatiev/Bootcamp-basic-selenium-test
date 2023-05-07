from selenium.webdriver.common.by import By


class VerificationPage:

    def __init__(self, driver):
        self.driver = driver

    def input_invalid_code(self):
        self.driver.find_element(By.XPATH, '//input[@id ="code"]').send_keys("123456789")
        self.driver.find_element(By.XPATH, '//button[text() ="Verify"]').click()

    def check_code_must_be_six_digits_error(self):
        return self.driver.find_element(By.XPATH, '//div[text() ="The authentication code must be 6 digits."]')

    def input_incorrect_code(self):
        self.driver.find_element(By.XPATH, '//input[@id ="code"]').clear()
        self.driver.find_element(By.XPATH, '//input[@id ="code"]').send_keys("000000")
        self.driver.find_element(By.XPATH, '//button[text() ="Verify"]').click()

    def check_incorrect_code_error(self):
        return self.driver.find_element(By.XPATH, '//div[text() ="Invalid authentication code, please try again"]')

