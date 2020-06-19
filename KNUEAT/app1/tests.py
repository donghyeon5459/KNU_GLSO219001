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
    name = driver.find_element_by_id("user_info")
    mypage = driver.find_element_by_link_text("마이페이지")
    assert "마이페이지" in mypage.text
    assert "로그아웃" in logout.text
    time.sleep(10)

def logout(driver):
    loginbutton = driver.find_element_by_link_text("로그아웃")
    loginbutton.click()

    login = driver.find_element_by_link_text("로그인")
    signup = driver.find_element_by_link_text("회원가입")

    assert "로그인" in login.text
    assert "회원가입" in signup.text
    time.sleep(10)


def shutdown(driver):
    
    driver.close()


if __name__ == '__main__':
    driver=setup()
    login(driver)
    logout(driver)