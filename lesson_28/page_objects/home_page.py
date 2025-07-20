from selenium.webdriver.common.by import By

class HomePageLocators:
    SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Sign In']")
    REGISTRATION_TAB = (By.XPATH, "//button[text()='Registration']")