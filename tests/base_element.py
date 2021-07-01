from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):
    """
    BaseElement
    Methods for the base element
    Методы элементов
    """
    def __init__(self, locator, driver):
        self.driver = driver
        self.locator = locator
        self.url = ''

        self.web_element = None
        self.wait = WebDriverWait(self.driver, 10)
        self.find()

    def find(self):
        """
        Finds an element at the initial run in __init__
        Находит элементы. Используется по умолчанию.
        :return:
        """
        element = self.wait.until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element

        return None

    def click(self):
        """
        Clicks the element that was found in self.find()
        Нажатие мышкой на элементы, найденные через self.find()
        :return:
        """
        element = self.wait.until(EC.element_to_be_clickable(locator=self.locator))
        element.click()

        return None

    def input_text(self, txt):
        """
        Inputs text into the input field
        Вставляет текст в поле ввода
        :param txt: pass in the text value
        :return:
        """
        self.web_element.send_keys(txt)
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    @property
    def text(self):
        """
        Returns the text received from the element
        Возвращает текст внутри элемента
        :return: text
        """
        text = self.web_element.text
        return text
