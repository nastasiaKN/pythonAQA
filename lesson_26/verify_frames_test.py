from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("http://localhost:8000/dz.html")

def handle_frame(frame_id, input_id, secret_text):
    driver.switch_to.frame(driver.find_element(By.ID, frame_id))
    driver.find_element(By.ID, input_id).send_keys(secret_text)
    driver.find_element(By.TAG_NAME, "button").click()
    alert = Alert(driver)
    time.sleep(0.5)
    assert "успішно" in alert.text
    alert.accept()
    driver.switch_to.default_content()

handle_frame("frame1", "input1", "Frame1_Secret")
handle_frame("frame2", "input2", "Frame2_Secret")

print("Both verifications passed.")
driver.quit()