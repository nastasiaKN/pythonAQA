from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegistrationPageLocators:
    NAME = (By.ID, "signupName")
    LAST_NAME = (By.ID, "signupLastName")
    EMAIL = (By.ID, "signupEmail")
    PASSWORD = (By.ID, "signupPassword")
    REPEAT_PASSWORD = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Register')]")

class RegistrationPage(BasePage):
    def fill_registration_form(self, name, last_name, email, password):
        self.find(RegistrationPageLocators.NAME).send_keys(name)
        self.find(RegistrationPageLocators.LAST_NAME).send_keys(last_name)
        self.find(RegistrationPageLocators.EMAIL).send_keys(email)
        self.find(RegistrationPageLocators.PASSWORD).send_keys(password)
        self.find(RegistrationPageLocators.REPEAT_PASSWORD).send_keys(password)

    def submit(self):
        self.find(RegistrationPageLocators.REGISTER_BUTTON).click()