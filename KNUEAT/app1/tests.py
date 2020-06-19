from django.test import TestCase
from selenium import webdriver
import time

# Create your tests here.

customerID = "knueat"
customerPW = "knueat"
def setup():
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    driver.get('http://127.0.0.1:8000/')

    time.sleep(10)
    return driver



def login(driver):
    loginbutton = driver.find_element_by_link_text("로그인")
    loginbutton.click()

    idBox = driver.find_element_by_name("userID")
    idBox.clear()
    idBox.send_keys(customerID)
    
    pwBox = driver.find_element_by_name("password")
    pwBox.clear()
    pwBox.send_keys(customerPW)

    loginSend = driver.find_element_by_xpath("//input[@value='로그인']")
    loginSend.click()

    logout = driver.find_element_by_link_text("로그아웃")
    print(logout.text)
    assert "로그아웃" in logout.text
    time.sleep(10)


def shutdown(driver):
    
    driver.close()


if __name__ == '__main__':
    driver=setup()
    login(driver)