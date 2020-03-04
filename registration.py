import pytest
from selenium import webdriver
import time

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_registration_test(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    browser.get(link)
    a = browser.find_element_by_id('login_link')
    a.click()
    input1 = browser.find_element_by_xpath('.//*[@name = "registration-email"]')
    input1.send_keys('tester12890@gmail.ru')
    input2 = browser.find_element_by_xpath('.//*[@name = "registration-password1"]')
    input2.send_keys('test4auth')
    input3 = browser.find_element_by_xpath('.//*[@name = "registration-password2"]')
    input3.send_keys('test4auth')
    button = browser.find_element_by_xpath('.//*[@name = "registration_submit"]')
    button.click()
    time.sleep(3)
    text1 = browser.find_element_by_xpath('.//*[@class="alertinner wicon"]')
    text = text1.text
    assert "Спасибо за регистрацию!" == text
