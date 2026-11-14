from pages.ShopPage import ShopPage


def test_shop(driver):
    page = ShopPage(driver)
    page.authorization()
    page.get_products()
    page.basket()
    page.checkout()
    page.form_input()
    assert page.get_total() == "$58.29", (
        f"Ожидали $58.29, получили {page.get_total()}"
    )
