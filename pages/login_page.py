from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.url
        assert "/login" in current_url, "Wrong URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_line = self.browser.find_element(*LoginPageLocators.EMAIL_LINE)
        email_line.send_keys(email)

        password1_line = self.browser.find_element(*LoginPageLocators.PASSWORD1_LINE)
        password1_line.send_keys(password)

        password2_line = self.browser.find_element(*LoginPageLocators.PASSWORD2_LINE)
        password2_line.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.SUBMIT_REGISTER)
        button.click()
