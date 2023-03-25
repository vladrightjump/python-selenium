import pytest
import time

from page_objects.log_in_succesful import LoggedInSuccesfullyPage
from page_objects.login_page import LoginPage
from selenium.webdriver.common.by import By


class TestNegativeScenarius:

    @pytest.mark.negative
    @pytest.mark.login
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("student99", "Password123", "Your username is invalid!"),
                              ("student", "password1234", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        logged_in_page = LoggedInSuccesfullyPage(driver)
        # Test case 1: Positive LogIn test
        # Open page
        login_page.open()
        login_page.execute_login(username, password)

        assert login_page.get_error_message() == expected_error_message, "Error message is not displayd, but it should"


