from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    BUTTON_7 = (By.XPATH, "//span[normalize-space()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[normalize-space()='+']")
    BUTTON_8 = (By.XPATH, "//span[normalize-space()='8']")
    BUTTON_RESULTS = (By.CSS_SELECTOR, ".btn.btn-outline-warning")
    RESULT_TEXT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver,
                 url="https://bonigarcia.dev/selenium-"
                     "webdriver-java/slow-calculator.html"):
        self.driver = driver
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

    def set_delay(self, value):
        delay_input = self.wait.until(EC.presence_of_element_located(
            self.DELAY_INPUT
        ))
        delay_input.clear()
        delay_input.send_keys(value)

    def calculate(self):
        self.driver.find_element(*self.BUTTON_7).click()
        self.driver.find_element(*self.BUTTON_PLUS).click()
        self.driver.find_element(*self.BUTTON_8).click()
        self.driver.find_element(*self.BUTTON_RESULTS).click()

    def wait_result(self, expected, timeout=45):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.RESULT_TEXT, expected))

    def get_result(self):
        return self.driver.find_element(*self.RESULT_TEXT).text
