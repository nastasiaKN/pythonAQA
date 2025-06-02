from lesson_10.homework_10 import log_event

def get_last_log_line():
    with open('login_system.log', 'r') as file:
        lines = file.readlines()
        return lines[-1] if lines else ''

def test_log_event_success():
    username = "user1"
    status = "success"
    log_event(username, status)

    last_log = get_last_log_line()
    assert username in last_log, "Username not found in log"
    assert status in last_log, "Status not found in log"

def test_log_event_expired():
    username = "user2"
    status = "expired"
    log_event(username, status)

    last_log = get_last_log_line()
    assert username in last_log, "Username not found in log"
    assert status in last_log, "Status not found in log"

def test_log_event_failed():
    username = "user3"
    status = "failed"
    log_event(username, status)

    last_log = get_last_log_line()
    assert username in last_log, "Username not found in log"
    assert status in last_log, "Status not found in log"