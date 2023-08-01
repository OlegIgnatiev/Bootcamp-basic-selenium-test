from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_driver(browser: str):
    if browser.upper() == "CH":
        driver = webdriver.Chrome(service=Service())
    elif browser.upper() == "CH_HL":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(), options=options)
    else:
        raise KeyError(
            f"Unexpected browser '{browser.upper()}'." f"Check your behave.ini file for available variables.")
    driver.set_window_size(width=1200, height=800)
    return driver
