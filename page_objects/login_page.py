from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field =(By.ID, "username")
    __password_field=(By.NAME, "password")
    __submit_buton= (By.XPATH, "/html//button[@id='submit']")
    __error_message= (By.ID, "error")

    def __int__(self,driver: WebDriver):
        super().__int__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str,password: str):
        super()._type(self.__username_field,username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_buton)

    def get_error_message(self)-> str:
        return super()._get_element_text(self.__error_message,time=3)


