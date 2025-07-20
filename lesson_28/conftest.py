import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.page_objects.home_page import HomePageLocators
from lesson_28.page_objects.registration_page import RegistrationPageLocators

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()

@pytest.fixture
def open_registration_tab(driver):
    wait = WebDriverWait(driver, 10)
    sign_in_button = wait.until(EC.element_to_be_clickable(HomePageLocators.SIGN_IN_BUTTON))
    sign_in_button.click()

    registration_tab = wait.until(EC.element_to_be_clickable(HomePageLocators.REGISTRATION_TAB))
    registration_tab.click()


    wait.until(EC.visibility_of_element_located(RegistrationPageLocators.NAME))

@pytest.fixture
def register_user(driver, open_registration_tab):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(RegistrationPageLocators.NAME)).send_keys("Test")
    driver.find_element(*RegistrationPageLocators.LAST_NAME).send_keys("User")
    driver.find_element(*RegistrationPageLocators.EMAIL).send_keys("testuser@example.com")
    driver.find_element(*RegistrationPageLocators.PASSWORD).send_keys("Password123")
    driver.find_element(*RegistrationPageLocators.REPEAT_PASSWORD).send_keys("Password123")
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()