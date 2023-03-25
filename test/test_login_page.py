import time

import pytest
from page_objects.log_in_succesful import LoggedInSuccesfullyPage
from page_objects.login_page import LoginPage



class TestPositiveScenarius:
    @pytest.mark.login
    @pytest.mark.pom
    @pytest.mark.positive
    def test_positive_login(self,driver):


        login_page= LoginPage(driver)
        logged_in_page = LoggedInSuccesfullyPage(driver)
        # Test case 1: Positive LogIn test
        # Open page
        login_page.open()
        login_page.execute_login("student","Password123")

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        assert logged_in_page.current_url == logged_in_page.current_url, "Actual URL is not the same as expected "
        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        assert logged_in_page.header == "Logged In Successfully", "Header is not expected"
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"
