from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

def handle_frame(driver, frame_id, input_id, secret_text):
    time.sleep(1)

    WebDriverWait(driver, 5).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, frame_id))
    )
    driver.find_element(By.ID, input_id).send_keys(secret_text)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(0.5)

    alert = Alert(driver)
    assert "успішно" in alert.text.lower()
    alert.accept()
    driver.switch_to.default_content()