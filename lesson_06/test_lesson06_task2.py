from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "YjkyMzU5YzktZmM4OC00Zjc1LWI0MTAtZTVkNDQ0ODUwODc2j",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru",
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/111test111")

    cookie1 = "https://gitflic.ru/user/111test111"
    driver.delete_all_cookies()

    driver.add_cookie({
        "name": "SESSION",
        "value": "Y2NhMDMwYmYtMjRiNC00YzYxLThlNDMtNzE5OTQxNWY3ZDM3",
        "domain": "gitflic.ru"
    })
    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru",
    })
    driver.refresh()
    driver.get("https://gitflic.ru/user/222test222")

    cookie2 = "https://gitflic.ru/user/222test222"
    driver.delete_all_cookies()

    assert cookie1 != cookie2

    driver.quit()
