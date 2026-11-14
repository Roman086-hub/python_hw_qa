from pages.CalculatorPage import CalculatorPage


def test_02_calc(driver):
    page = CalculatorPage(driver)
    page.set_delay("45")
    page.calculate()
    page.wait_result("15")
    assert page.get_result() == "15", "Результат не равен 15"
