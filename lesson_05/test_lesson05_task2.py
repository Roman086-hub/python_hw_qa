from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(1)
    (driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='Customer name']")
        .send_keys("Roman"))

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert driver.current_url == "https://httpbin.qa-territory.online/post"

    driver.quit()
