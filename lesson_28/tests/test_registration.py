from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from lesson_28.page_objects.home_page import HomePageLocators
from lesson_28.page_objects.registration_page import RegistrationPageLocators

def test_user_registration(driver, registration_page):
    wait = WebDriverWait(driver, 10)


    wait.until(EC.element_to_be_clickable(HomePageLocators.SIGN_IN_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(HomePageLocators.REGISTRATION_TAB)).click()
    wait.until(EC.visibility_of_element_located(RegistrationPageLocators.NAME))


    registration_page.fill_registration_form(
        name="Test", last_name="User", email="testuser@example.com", password="Password123"
    )
    registration_page.submit()


    assert driver.title == "Hillel Qauto"