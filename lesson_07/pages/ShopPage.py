from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    USER = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCT_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    PRODUCT_BOLT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    PRODUCT_ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    BASKET_BUTTON = (By.XPATH, "//a[@aria-label='Cart, 3 items']")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    SUMMARY_TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver, url="https://www.saucedemo.com/"):
        self.driver = driver
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

    def authorization(self):
        self.driver.find_element(*self.USER).send_keys("standard_user")

        self.driver.find_element(*self.PASSWORD).send_keys("secret_sauce")

        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_products(self):
        self.wait.until(EC.element_to_be_clickable(
            self.PRODUCT_BACKPACK)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.PRODUCT_BOLT)).click()
        self.wait.until(EC.element_to_be_clickable(
            self.PRODUCT_ONESIE)).click()

    def basket(self):
        self.wait.until(EC.element_to_be_clickable(
            self.BASKET_BUTTON)).click()

    def checkout(self):
        self.wait.until(EC.element_to_be_clickable(
            self.CHECKOUT_BUTTON)).click()

    def form_input(self):
        self.wait.until(EC.presence_of_element_located(
            self.FIRST_NAME)).send_keys("Roman")
        self.wait.until(EC.presence_of_element_located(
            self.LAST_NAME)).send_keys("Potapov")
        self.wait.until(EC.presence_of_element_located(
            self.POSTAL_CODE)).send_keys("143430")
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total(self):
        total = self.wait.until(EC.presence_of_element_located(
            self.SUMMARY_TOTAL))
        return total.text.strip().replace("Total: ", "")
