from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        # Ожидаем, что в корзине нет товаров
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "Basket is not empty"

    def should_be_empty_msg(self):
        # Ожидаем, что есть текст о том что корзина пуста
        msg_link = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MSG)
        msg = msg_link.get_attribute("href")

        assert msg != "#voucher", "Basket has not empty message"
