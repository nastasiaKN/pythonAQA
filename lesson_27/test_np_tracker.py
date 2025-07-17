import pytest
from NP_tracker import NovaPoshtaTracker

class TestNovaPoshta:

    def test_nova_poshta_status(self, tracker):
        tracking_number = "59001375336472"
        expected_status = "Посилка отримана"

        status = tracker.track(tracking_number)
        assert "Отримана" in status, f"Expected status to contain 'Отримана', got '{status}'"