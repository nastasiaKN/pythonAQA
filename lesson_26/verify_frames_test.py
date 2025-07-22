from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_frame1_verification(driver):
    time.sleep(1)
    WebDriverWait(driver, 5).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1"))
    )

    driver.find_element(By.ID, "input1").send_keys("Frame1_Secret")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(0.5)

    alert = Alert(driver)
    alert_text = alert.text
    assert "успішно" in alert_text.lower()
    alert.accept()
    driver.switch_to.default_content()


def test_frame2_verification(driver):
    time.sleep(1)
    WebDriverWait(driver, 5).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "frame2"))
    )

    driver.find_element(By.ID, "input2").send_keys("Frame2_Secret")
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(0.5)

    alert = Alert(driver)
    alert_text = alert.text
    assert "успішно" in alert_text.lower()
    alert.accept()
    driver.switch_to.default_content()