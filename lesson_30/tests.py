import allure

@allure.feature("Math operations")
@allure.story("Sum calculation")
@allure.title("Sum of two numbers")
@allure.severity(allure.severity_level.NORMAL)
def test_sum():
    with allure.step("Calculate sum of 2 + 2"):
        result = 2 + 2
    with allure.step("Check if result is 4"):
        assert result == 4, "Expected 4"