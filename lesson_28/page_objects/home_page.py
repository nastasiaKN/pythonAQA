from selenium.webdriver.common.by import By

class HomePageLocators:
    SIGN_IN_BUTTON = (By.XPATH, "//button[normalize-space()='Sign In']")
    REGISTRATION_TAB = (By.XPATH, "//button[normalize-space()='Registration']")