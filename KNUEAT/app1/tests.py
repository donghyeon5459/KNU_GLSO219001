from django.test import TestCase
from selenium import webdriver
import time

# Create your tests here.

customerID = "knueat"
customerPW = "knueat"
ownerID = "knueat2"
ownerPW = "knueat2"
signUpID = "knueat10"
signUpPW = "knueat10"
signUpName = "knueat10"
phoneNumber = "01012345678"

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

    loginSubmit = driver.find_element_by_xpath("//input[@value='로그인']")
    loginSubmit.click()

    logout = driver.find_element_by_link_text("로그아웃")
    name = driver.find_element_by_id("user_info")
    mypage = driver.find_element_by_link_text("마이페이지")
    assert "마이페이지" in mypage.text
    assert "로그아웃" in logout.text
    time.sleep(10)

def loginOwner(driver) :
    loginbutton = driver.find_element_by_link_text("로그인")
    loginbutton.click()

    idBox = driver.find_element_by_name("userID")
    idBox.clear()
    idBox.send_keys(ownerID)
    
    pwBox = driver.find_element_by_name("password")
    pwBox.clear()
    pwBox.send_keys(ownerPW)

    loginSubmit = driver.find_element_by_xpath("//input[@value='로그인']")
    loginSubmit.click()

    logout = driver.find_element_by_link_text("로그아웃")
    name = driver.find_element_by_id("user_info")
    mypage = driver.find_element_by_link_text("마이페이지")
    assert "마이페이지" in mypage.text
    assert "로그아웃" in logout.text
    time.sleep(10)

def logout(driver):
    logoutButton = driver.find_element_by_link_text("로그아웃")
    logoutButton.click()

    login = driver.find_element_by_link_text("로그인")
    signup = driver.find_element_by_link_text("회원가입")

    assert "로그인" in login.text
    assert "회원가입" in signup.text
    time.sleep(10)

def signup(driver):
    signupButton = driver.find_element_by_link_text("회원가입")
    signupButton.click()

    idBox = driver.find_element_by_name("userID")
    idBox.clear()
    idBox.send_keys(signUpID)
    
    pwBox = driver.find_element_by_name("password1")
    pwBox.clear()
    pwBox.send_keys(signUpPW)

    pwBox2 = driver.find_element_by_name("password2")
    pwBox2.clear()
    pwBox.send_keys(signUpPW)

    name = driver.find_element_by_name("name")
    name.clear()
    name.send_keys(signUpName)

    phone = driver.find_element_by_name("phone")
    phone.clear()
    phone.send_keys(phoneNumber)

    selectTypeCus = driver.find_element_by_xpath("//input[@value='고객']")
    selectTypeCus.click()

    signUpSubmit = driver.find_element_by_xpath("//input[@value='고객']")
    signUpSubmit.click()

def recommend_non_members(driver) :
    recommend = driver.find_element_by_xpath("//h3")
    img = driver.find_element_by_class_name('card-image2')
    assert "오늘의 추천" in recommend.text
    assert img.is_displayed()

def recommend_members(driver) :
    login(driver)
    recommend = driver.find_element_by_xpath("//h3")
    img = driver.find_element_by_class_name('card-image2')
    assert "님을 위한 오늘의 추천" in recommend.text
    assert img.is_displayed()

def recommend_no_reservation(driver):
    loginOwner(driver)
    recommend = driver.find_element_by_xpath("//h3")
    img = driver.find_element_by_class_name('card-image2')
    assert "님을 위한 오늘의 추천" in recommend.text
    assert img.is_displayed()

def search(driver):
    restaurantName = "대독장"
    #driver.get('http://127.0.0.1:8000/')
    searchBar = driver.find_element_by_xpath("//input[@class='search_box']")
    searchBar.clear()
    searchBar.send_keys(restaurantName)

    searchButton = driver.find_element_by_xpath("//input[@class='search_btn']")
    searchButton.click()

    title = driver.find_element_by_xpath("//h1")
    #assert restaurantName in title.text, "Error : 식당 이름이 검색 결과 문장에 나오지 않습니다."
    #assert "결과입니다" in title.text
    cardImage = driver.find_element_by_xpath("//img[@src]")
    cardTitle = driver.find_element_by_xpath("//p[@class='card-title']")
    cardRestaurant = driver.find_element_by_xpath("//div[@class='restaurant']")

    assert cardImage, cardTitle in cardRestaurant
    if cardRestaurant:
        assert cardImage.is_displayed(), "Error @search : 식당 이미지가 표시되지 않았습니다."
        assert cardTitle.is_displayed(), "Error @search : 식당 이름이 표시되지 않았습니다."



def shutdown(driver):
    
    driver.close()


if __name__ == '__main__':
    driver=setup()
    #login(driver)
    #logout(driver)
    #signup(driver)
    #recommend_non_members(driver)
    #recommend_members(driver)
    #recommend_no_reservation(driver)
    search(driver)