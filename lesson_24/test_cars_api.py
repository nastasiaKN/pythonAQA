import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

# Налаштування логування
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('test_search.log', mode='w')
console_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)


@pytest.fixture(scope="class")
def auth_session(request):
    session = requests.Session()
    auth_data = HTTPBasicAuth('test_user', 'test_pass')

    response = session.post(f"{BASE_URL}/auth", auth=auth_data)
    assert response.status_code == 200, "Authentication failed"

    token = response.json().get("access_token")
    assert token, "No token received"

    session.headers.update({"Authorization": f"Bearer {token}"})
    request.cls.session = session


@pytest.mark.usefixtures("auth_session")
class TestCarSearch:

    @pytest.mark.parametrize("sort_by,limit", [
        ("price", 2),
        ("year", 3),
        ("engine_volume", 5),
        ("brand", 4),
        ("price", 10),
        ("year", 1),
        ("", 3),  # Без сортування
    ])
    def test_car_search(self, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        params["limit"] = limit

        logger.info(f"Testing with params: {params}")
        response = self.session.get(f"{BASE_URL}/cars", params=params)
        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response: {response.text}")

        assert response.status_code == 200, f"Failed request with params {params}"
        cars = response.json()
        assert isinstance(cars, list), "Response is not a list"
        assert len(cars) <= limit, f"Returned more cars than expected: {len(cars)} > {limit}"