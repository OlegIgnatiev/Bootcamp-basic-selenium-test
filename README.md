# Bootcamp-basic-selenium-test
These tests are written in the Python UnitTest framework.
# Structure Unittest
In 'selenium_tests' folder you can find 'test_selenium.py' file with assertions, call of methods from 'pages' and 3 tests: login_validation, 2FA_verification, reset_password.
In 'pages' folder you can find three page_object files: credentials_page, forgrot_password_page, Verification_page. These files describe methods, behaviour and logic.
And also 'base_page' file located in 'pages' folder. This filed include exceptions, timeouts, waits and other basic logic.

![files in project](https://github.com/OlegIgnatiev/Bootcamp-basic-selenium-test/assets/119042843/f6d9ea4d-f897-4d69-b3ea-edfaab40535b)
# Run tests Unittest
To run a test you should have Python3 on your machine, pipenv, files mentioned in structure downloaded, set route to this project and run the command:
python -m unittest selenium_tests/test_selenium.py

# Structure and using BDD framework
This stack using: behave, selenium, pyhamcrest
To use it, you should have Python3 on your machine, pipenv, files mentioned in structure downloaded, set route to this project and run the command: invoke run. Also you can set parameters to choose test scenario by tag and browser. For example: **invoke run --tags:mfa --browser=CH_HL**. This command will start MFA test without opening browser.

