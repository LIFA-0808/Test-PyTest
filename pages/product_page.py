from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_able_to_add_product_to_basket(self):
        self.should_be_add_product_to_basket()
        self.should_be_message_about_adding_to_basket()
        self.should_be_basket_price()

    # метод для добавления товара в корзину
    def should_be_add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    # методы-проверки
    def should_be_message_about_adding_to_basket(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_TITLE).text
        assert name == alert_name, "Wrong Product name"

    def should_be_basket_price(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_MINI).text
        alert_basket = self.browser.find_element(*ProductPageLocators.ALERT_BASKET).text
        assert basket == alert_basket, "Wrong Basket sum"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should was"
