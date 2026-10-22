from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
    wait = WebDriverWait(driver, 10)

    delay_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(
        By.XPATH, "//span[normalize-space()='7']").click()
    driver.find_element(
        By.XPATH, "//span[normalize-space()='+']").click()
    driver.find_element(
        By.XPATH, "//span[normalize-space()='8']").click()
    driver.find_element(
        By.CSS_SELECTOR, ".btn.btn-outline-warning").click()

    result = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15")
    )
    assert result, "Результат не равен 15"

    driver.quit()
