from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_in_basket(self):
        self.should_be_price()
        self.should_be_button_add_basket()
        self.browser.find_element(*ProductPageLocators.ADD_BASKET).click()

    def check_product_in_basket(self):
        self.should_be_right_final_price()
        self.should_be_right_final_name()

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Price is not presented"

    def should_be_button_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "Basket is not presented"

    def should_be_right_final_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_BASKET), "The final price is not presented"
        assert (self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text ==
                self.browser.find_element(*ProductPageLocators.PRICE).text), "The final price is incorrect"

    def should_be_right_final_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), "The final name is not presented"
        assert (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text ==
                self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text), "The final name product is incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"