from .locator import Locator
from .base_element import BaseElement
from .base_page import BasePage
from selenium.webdriver.common.by import By


class CheckAuth(BasePage):
    """
    The auth page at vk.com/
    """

    url = 'https://vk.com'

    @property
    def email_check(self):
        """
        Email/phone number field
        Поле почты/номера телефона
        :return:
        """
        locator = Locator(by=By.ID, value='index_email')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def pass_check(self):
        """
        Password field
        Поле пароля
        :return:
        """
        locator = Locator(by=By.ID, value='index_pass')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def login(self):
        """
        Press the login button
        Нажатие кнопки "Войти"
        :return:
        """
        locator = Locator(by=By.ID, value='index_login_button')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
