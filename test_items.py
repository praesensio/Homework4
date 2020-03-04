from selenium import webdriver
import time

link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30) #sleep для проверки правильности инициализации браузера
    assert browser.find_element_by_css_selector('.btn-add-to-basket'), "Here is no button"
