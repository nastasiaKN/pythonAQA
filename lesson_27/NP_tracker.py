import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NovaPoshtaTracker:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)

    def open(self):
        self.driver.get("https://tracking.novaposhta.ua/#/uk")

    def track(self, number: str) -> str:
        input_elem = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input.track__form-group-input")
        ))
        input_elem.send_keys(number)

        search_button = self.driver.find_element(By.ID, "np-number-input-desktop-btn-search-en")
        search_button.click()

        self.wait.until(EC.url_contains("/chat/messages"))
        time.sleep(2)

        try:
            close_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Добре')]"))
            )
            close_btn.click()
        except Exception:
            pass

        status_elem = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[contains(text(),'Отримана') or contains(text(),'Доставлено')]")
        ))
        return status_elem.text.strip()

    def close(self):
        self.driver.quit()