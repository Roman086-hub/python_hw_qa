from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
    wait = WebDriverWait(driver, 10)

    fields = [
            ("first-name", "Иван"),
            ("last-name", "Петров"),
            ("address", "Ленина, 55-3"),
            ("e-mail", "test@skypro.com"),
            ("phone", "+7985899998787"),
            ("city", "Москва"),
            ("country", "Россия"),
            ("job-position", "QA"),
            ("company", "SkyPro"),
        ]

    for name, value in fields:
        field = wait.until(EC.presence_of_element_located((By.NAME, name)))
        field.send_keys(value)

    submit_btn = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")))
    submit_btn.click()

    zip_code_field = wait.until(EC.presence_of_element_located(
        (By.ID, "zip-code")))

    classes = zip_code_field.get_attribute("class") or ""
    assert "alert-danger" in classes or "alert-success" in classes, (
        f"Zip code не подсвечен ошибкой. Классы: {classes}"
        )

    valid_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
        ]

    for name in valid_fields:

        field = wait.until(EC.presence_of_element_located((By.ID, name)))
        classes = field.get_attribute("class") or ""

    assert "success" in classes or "valid" in classes, \
        f"Поле '{name}' не подсвечено как валидное. Классы: '{classes}'"

    driver.quit()
