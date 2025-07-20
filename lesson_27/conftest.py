import pytest
from NP_tracker import NovaPoshtaTracker

@pytest.fixture
def tracker():
    tracker = NovaPoshtaTracker()
    tracker.open()
    yield tracker
    tracker.close()