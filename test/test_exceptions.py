
import  pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.exceptions_pom import Exceptions
class TestExceptions:



    @pytest.mark.element

    def test_no_such_element_exception(self,driver):
        # Open page
        exceptions_page= Exceptions(driver)
        exceptions_page.open()
        # Click Add button
        exceptions_page.click_add_button()
        # Verify Row 2 input field is displayed
        assert exceptions_page.row2_inputfild_is_displayd(), "Row two should be displayed but is not"

    @pytest.mark.element

    def test_element_not_intreractable_exception(self, driver):
        # Open page
        exceptions_page = Exceptions(driver)
        exceptions_page.open()
        # Click Add button
        exceptions_page.click_add_button()

        text ="Pasta"
        exceptions_page.row2_type_in_the_input_field(text)
        # Push Save button using locator By.name(“Save”)

        exceptions_page.row2_click_button_save()
        # Verify text saved

        confirmation_message = "Row 2 was saved"
        assert exceptions_page.confirmation_message_is_displayd() == confirmation_message

    @pytest.mark.element
    def test_invalid_element_state_exception_for_row_2(self,driver):
        # Open page
        exceptions_page = Exceptions(driver)
        exceptions_page.open()
        # Click Add button
        exceptions_page.click_add_button()

        text = "Pasta"
        exceptions_page.row2_type_in_the_input_field(text)
        # Push Save button using locator By.name(“Save”)

        exceptions_page.row2_click_button_save()
        # Verify text saved

        confirmation_message = "Row 2 was saved"
        assert exceptions_page.confirmation_message_is_displayd() == confirmation_message

        # Clear input field
        exceptions_page.row2_clear_the_input_field()
        # Type text into the input field
        food= 'Ice'
        exceptions_page.row2_type_in_the_input_field(food)
#       Verify text changed
        assert exceptions_page.confirmation_message_is_displayd() == confirmation_message

    @pytest.mark.element

    def test_invalid_element_state_exception(self, driver):
        # Open page
        exceptions_page = Exceptions(driver)
        exceptions_page.open()
        exceptions_page.row1_clear_the_input_field()
        food = 'Ice'
        exceptions_page.row1_type_in_the_input_field(food)
        exceptions_page.row1_click_button_save()
        #       Verify text changed

        assert exceptions_page.row1_check_the_value().get_attribute("value") == food, "Expected Ice , but got" + food
        # Verify text saved

        confirmation_message = "Row 1 was saved"
        assert exceptions_page.confirmation_message_is_displayd() == confirmation_message ,"Expected Row 1 was saved, but got "+confirmation_message

    @pytest.mark.element
    @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        # Open page
        exceptions_page = Exceptions(driver)
        exceptions_page.open()


        # Find the instructions text element

        instruction_element_message = "Push “Add” button to add another row"
        assert exceptions_page.instruction_message_is_displayd_and_has_text()  == instruction_element_message
        # Click Add button
        exceptions_page.click_add_button()
        # Verify Row 2 input field is displayed
        assert exceptions_page.row2_inputfild_is_displayd(), "Row two should be displayed but is not"

        # Verify instruction text element is no longer displayed

        assert exceptions_page.vladitation_that_instruction_no_longer_displayd(), "Instruction element should not be displayed"

    @pytest.mark.element

    def test_timeout_exception(self, driver):
        # Open page
        exceptions_page = Exceptions(driver)
        exceptions_page.open()

        # Find the instructions text element

        instruction_element_message = "Push “Add” button to add another row"
        assert exceptions_page.instruction_message_is_displayd_and_has_text() == instruction_element_message
        # Click Add button
        exceptions_page.click_add_button()
        # Verify Row 2 input field is displayed
        assert exceptions_page.row2_inputfild_is_displayd(), "Row two should be displayed but is not"





