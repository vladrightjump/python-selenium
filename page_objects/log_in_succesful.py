from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccesfullyPage(BasePage):
    __urt = "https://practicetestautomation.com/logged-in-successfully/"

    __text_locator = (By.CLASS_NAME, 'post-title')

    __log_out_locator = (By.LINK_TEXT, 'Log out')

    def __int__(self, driver: WebDriver):
        super().__int__(driver)

    @property
    def expected_urt(self) -> str:
        return self.__urt

    @property
    def header(self) -> str:
        return super()._get_element_text(self.__text_locator)

    def is_logout_button_displayed(self) -> bool:
        return super()._is_displayed(self.__log_out_locator)
