from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

#класс-предок в Python указывается в скобках
class MainPage(BasePage):
    def go_to_login_page(self):
        #здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"