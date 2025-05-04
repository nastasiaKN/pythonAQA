import pytest

from homework9_1 import (
    total_sea_area,
    calculate_items_per_warehouse,
    calculate_total_price,
    remain_from_num_devision,
    count_total_order_price,
    road_trip_stats,
    has_h,
    add_string_items_to_the_list,
    even_numbers_from_list
)

# Task 04
class TestTotalSeaArea:
    def test_positive(self):
        assert total_sea_area(436402, 37800) == 474202

    def test_negative(self):
        assert total_sea_area(436402, 37800) != 500000

# Task 05
class TestItemsPerWarehouse:
    def test_positive(self):
        assert calculate_items_per_warehouse(375291, 250449, 222950) == (152341, 98108, 124842)

    def test_negative(self):
        assert calculate_items_per_warehouse(375291, 250449, 222950) != (100000, 100000, 100000)

# Task 06
class TestTotalPrice:
    def test_positive(self):
        assert calculate_total_price(1179, 18) == 21222

    def test_negative(self):
        assert calculate_total_price(1179, 18) != 20000

# Task 07
class TestRemainFromDivision:
    def test_positive(self):
        values = [8019 % 8, 9907 % 9, 2789 % 5, 7248 % 6, 7128 % 5, 19224 % 9]
        assert remain_from_num_devision(values) == [3, 7, 4, 0, 3, 0]

    def test_negative(self):
        values = [8019 % 8, 9907 % 9, 2789 % 5, 7248 % 6, 7128 % 5, 19224 % 9]
        assert remain_from_num_devision(values) != [0, 0, 0, 0, 0, 0]

# Task 08
class TestOrderPrice:
    def test_positive(self):
        prices = {
            "pizza_L": 274,
            "pizza_M": 218,
            "juice": 35,
            "cake": 350,
            "water": 21
        }
        counts = {
            "pizza_L": 4,
            "pizza_M": 2,
            "juice": 4,
            "cake": 1,
            "water": 3
        }
        assert count_total_order_price(prices, counts) == 2085

    def test_negative(self):
        prices = {
            "pizza_L": 274,
            "pizza_M": 218,
            "juice": 35,
            "cake": 350,
            "water": 21
        }
        counts = {
            "pizza_L": 4,
            "pizza_M": 2,
            "juice": 4,
            "cake": 1,
            "water": 3
        }
        assert count_total_order_price(prices, counts) != 3000
# Task 09
class TestPagination:
    def test_positive(self):
        photos = 232
        per_page = 8
        expected_pages = (photos + per_page - 1) // per_page
        assert expected_pages == 29

    def test_negative(self):
        photos = 232
        per_page = 8
        assert (photos + per_page - 1) // per_page != 28

# Task 10
class TestRoadTripStats:
    def test_positive(self):
        assert road_trip_stats(1600, 9, 48) == (144.0, 3)

    def test_negative(self):
        assert road_trip_stats(1600, 9, 48) != (200, 4)

# Task 6.2
class TestHasH:
    def test_positive(self):
        assert has_h("Python") is True

    def test_negative(self):
        assert has_h("apple") is False
# Task 6.3
class TestAddStringItems:
    def test_positive(self):
        assert add_string_items_to_the_list(['1', 2, 'hi']) == ['1', 'hi']

    def test_negative(self):
        assert add_string_items_to_the_list([1, 2, 3]) == []
# Task 6.4
class TestEvenNumbers:
    def test_positive(self):
        assert even_numbers_from_list([2, 3, 4, 5, 6]) == [2, 4, 6]

    def test_negative(self):
        assert even_numbers_from_list([1, 3, 5]) == []