from lesson_10.homework_10 import log_event, logger

def test_log_event_success():
    username = "user1"
    status = "success"
    logger.info(f"Running test_log_event_success for username={username}, status={status}")
    log_event(username, status)

def test_log_event_expired():
    username = "user2"
    status = "expired"
    logger.info(f"Running test_log_event_expired for username={username}, status={status}")
    log_event(username, status)

def test_log_event_failed():
    username = "user3"
    status = "failed"
    logger.info(f"Running test_log_event_failed for username={username}, status={status}")
    log_event(username, status)