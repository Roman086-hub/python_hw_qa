from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_03_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
    wait.until(EC.element_to_be_clickable(
        (By.ID, "add-to-cart-sauce-labs-onesie"))).click()

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@aria-label='Cart, 3 items']"))).click()

    wait.until(EC.element_to_be_clickable(
        (By.ID, "checkout"))).click()

    wait.until(EC.presence_of_element_located(
        (By.ID, "first-name"))).send_keys("Roman")
    wait.until(EC.presence_of_element_located(
        (By.ID, "last-name"))).send_keys("Potapov")
    wait.until(EC.presence_of_element_located(
        (By.ID, "postal-code"))).send_keys("143430")

    driver.find_element(By.ID, "continue").click()

    total = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".summary_total_label")))
    total_text = total.text.strip()
    total_value = total_text.replace("Total: ", "")

    assert total_value == "$58.29", (
        f"Ожидалась сумма $58.29, но получено: {total_value}"
        )
    driver.quit()
