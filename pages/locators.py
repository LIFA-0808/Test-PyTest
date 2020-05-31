from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCTS_IN_BASKET = (By.ID, "basket_formset")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    EMAIL_LINE = (By.CSS_SELECTOR, "#id_registration-email.form-control")
    PASSWORD1_LINE = (By.CSS_SELECTOR, "#id_registration-password1.form-control")
    PASSWORD2_LINE = (By.CSS_SELECTOR, "#id_registration-password2.form-control")
    SUBMIT_REGISTER = (By.CSS_SELECTOR, ".register_form .btn")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BASKET_MINI = (By.CSS_SELECTOR, ".product_main .price_color")
    ALERT_TITLE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) .alertinner strong")
    ALERT_BASKET = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
