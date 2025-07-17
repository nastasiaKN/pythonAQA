import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)


    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, "dz.html")

    driver.get("file://" + html_path)

    yield driver
    driver.quit()