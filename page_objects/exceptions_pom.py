from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Exceptions(BasePage):
    __url='https://practicetestautomation.com/practice-test-exceptions/'
    __add_button = (By.ID,"add_btn")
    __input__field_two =(By.XPATH,"//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")
    __row2_button_save =(By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']")
    __confirmation_message_locator = (By.ID,'confirmation')
    __row2_edit_button_field = (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='edit_btn']")
    __row1_input_field = (By.XPATH, "//div[@id='rows']/div[1]/div[@class='row']/input[@value='Pizza']")
    __row1_edit_button = (By.XPATH, "/html//button[@id='edit_btn']")
    __row1_save__button =(By.XPATH, "/html//button[@id='save_btn']")
    __instruction_message= (By.XPATH,"/html//p[@id='instructions']")
    def __int__(self,driver: WebDriver):
        super().__init__(driver)

    def open(self):
        return super()._open_url(self.__url)

    def row2_inputfild_is_displayd(self)-> bool:
        super()._wait_until_element_is_visible(self.__input__field_two)
        return super()._is_displayed(self.__input__field_two)

    def click_add_button(self):
        return super()._click(self.__add_button)


    def row2_type_in_the_input_field(self, text:str):
        return super()._type(self.__input__field_two,text)

    def row2_click_button_save(self):
        super()._click(self.__row2_button_save)
    def confirmation_message_is_displayd(self) -> str:
        super()._wait_until_element_is_visible(self.__confirmation_message_locator)
        return super()._get_element_text(self.__confirmation_message_locator)

    def row2_clear_the_input_field(self):
        super()._click(self.__row2_edit_button_field)
        return super()._clear_the_input_fild(self.__input__field_two)

    def row1_clear_the_input_field(self):
        super()._click(self.__row1_edit_button)
        return super()._clear_the_input_fild(self.__row1_input_field)

    def row1_type_in_the_input_field(self, text: str):
        return super()._type(self.__row1_input_field,text)

    def row1_click_button_save(self):
        super()._click(self.__row1_save__button)


    def row1_check_the_value(self):
        return super()._find(self.__row1_input_field)
    def instruction_message_is_displayd_and_has_text(self):
        super()._is_displayed(self.__instruction_message)
        return super()._get_element_text(self.__instruction_message)
    def vladitation_that_instruction_no_longer_displayd(self):
        return super()._element_is_not_displayd(self.__instruction_message)