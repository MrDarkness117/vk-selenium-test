from .locator import Locator
from .base_element import BaseElement
from .base_page import BasePage
from selenium.webdriver.common.by import By


class VK(BasePage):

    url = 'https://vk.com'

    @property
    def messages(self):
        """
        The personal messages page
        Раздел "Сообщения"
        :return:
        """
        locator = Locator(by=By.ID, value='l_msg')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def select_msg(self, peer):
        """
        Select a chat following the data-peer value
        Выбрать диалог через peer id (id пользователя)
        :param peer:
        :return:
        """
        # locator = Locator(by=By.XPATH, value=('//li[contains(@data-peer, "' + str(peer) + '")]'))
        locator = Locator(by=By.CLASS_NAME, value=('_im_dialog_' + peer))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def msg_input_field(self):
        """
        The input field for messages
        Поле ввода сообщения
        :return:
        """
        locator = Locator(by=By.ID, value='im_editable0')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def btn_send_msg(self):
        """
        Send message button
        Кнопка отправки сообщения
        :return:
        """
        locator = Locator(
            by=By.CLASS_NAME,
            value="im-chat-input--send"
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def user_name(self, peer):
        """
        Fetch the peer first name and second name
        Получить имя, фамилию пользователя через peer id
        :param peer:
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//li[contains(@data-peer, "'
                  + peer + '")]/div/div/div/span/span[contains(@class, "_im_dialog_link")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

