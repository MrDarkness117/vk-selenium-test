from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# TODO: Requires Selenium to run: "pip install selenium"
# TODO: Необходима библиотека Selenium!
from tests.auth_control import CheckAuth
from tests.auth_passed import VK

email = '<email>'
password = '<pass>'

peer = '<peer_id>'

# Test Setup
options = Options()
browser = webdriver.Chrome(chrome_options=options)
browser.set_window_position(0, 0)
browser.maximize_window()
auth_passed = False


# Auth Page
vk = CheckAuth(driver=browser)
vk.go()
if vk.url == 'https://vk.com':
    vk.email_check.input_text(email)
    vk.pass_check.input_text(password)
    vk.login.click()
    auth_passed = True

# VK Page
if vk.url == 'https://vk.com/feed' or auth_passed:
    print('Auth Success!')
    vk = VK(driver=browser)
    vk.messages.click()
    vk.select_msg(peer).click()
    vk.select_msg(peer).click()
    vk.msg_input_field.input_text('Проверка работы Selenium на пользователе: ' + vk.user_name(peer).text)
    vk.btn_send_msg.click()
    time.sleep(1)
    vk.msg_input_field.input_text('Привет, ' + vk.user_name(peer).text)
    vk.btn_send_msg.click()
    time.sleep(1)

print("Finished.")
browser.quit()
