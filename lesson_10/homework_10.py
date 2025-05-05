import logging
import os


log_path = os.path.join(os.path.dirname(__file__), "login_system.log")
print("log will be written to:", log_path)


logger = logging.getLogger("log_event")
logger.setLevel(logging.INFO)


for handler in logger.handlers[:]:
    logger.removeHandler(handler)


file_handler = logging.FileHandler(log_path, mode='a', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)