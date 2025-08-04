import allure

@allure.feature("Math operations")
@allure.story("Sum calculation")
@allure.title("Sum of two numbers")
@allure.severity(allure.severity_level.NORMAL)
def test_sum():
    a = 2
    b = 2
    expected_result = 4

    with allure.step(f"Calculate sum of {a} + {b}"):
        result = a + b

    with allure.step(f"Check if result is {expected_result}"):
        assert result == expected_result, f"Expected {expected_result}, but got {result}"