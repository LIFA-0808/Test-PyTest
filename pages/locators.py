from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_MINI = (By.CSS_SELECTOR, ".basket-mini")
    ALERT_TITLE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner strong")
    ALERT_BASKET = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")
