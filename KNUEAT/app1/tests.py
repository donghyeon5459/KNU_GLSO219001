from django.test import TestCase
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

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

    time.sleep(10)
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


def clickCategoryImage(driver):
    categoryNum = 6
    for i in range(1, categoryNum):
        categoriesImg = driver.find_element_by_xpath("(//p[@class='card-image'])["+str(i)+"]")
        categoriesTitle = driver.find_element_by_xpath("(//p[@class='card-title'])["+str(i)+"]")
        categoryTitleText = categoriesTitle.text
        categoriesImg.click()
        time.sleep(5)
        #for category in categories :
        
        #category.click()

        categoryHeader = driver.find_element_by_xpath("//div[@class='page-header']")
        
        assert categoryTitleText in categoryHeader.text, "Error @clickCategory : 카테고리 이름이 표시되지 않았습니다."
        print("success")
        homeButton = driver.find_element_by_xpath("//a[@href = '/']")
        homeButton.click()
        time.sleep(5)


def clickCategoryText(driver):
    categoryNum = 6
    for i in range(1, categoryNum):
        categories = driver.find_element_by_xpath("(//p[@class='card-title'])["+str(i)+"]")
        categoryTitle = categories.text
        categories.click()
        time.sleep(5)

        categoryHeader = driver.find_element_by_xpath("//div[@class='page-header']")
        
        assert categoryTitle in categoryHeader.text, "Error @clickCategory : 카테고리 이름이 표시되지 않았습니다."
        print("success")
        homeButton = driver.find_element_by_xpath("//a[@href = '/']")
        homeButton.click()
        time.sleep(5)
    
def clickRestaurant(driver) :
    i = 1
    category = driver.find_element_by_xpath("(//p[@class='card-title'])["+str(i)+"]")
    category.click()
    time.sleep(5)

    restaurant = driver.find_element_by_xpath("//div[@class='restaurant']/a")
    #restaurantA = restaurant.find_element_by_xpath("/a")
    assert restaurant, "식당 리스트가 뜨지 않았습니다."
    restaurant.click()
    time.sleep(5)
    restaurantInfo = driver.find_element_by_xpath("//div[@class='restaurant_info']")
    assert restaurantInfo, "식당 정보가 뜨지 않았습니다."

def restaurantInformation(driver):
    #평점, 즐겨찾기 버튼, 즐겨찾기한 사용자 수, 전화번호, 주소, 오픈 시간, 마감 시간, 정보, 메뉴, 리뷰를 보여준다.
    clickRestaurant(driver)
    restaurantText = driver.find_element_by_xpath("//div[@class='restaurant_info']")

    assert restaurantText.is_displayed(), "Error @restaurantInformation : 가게 정보가 나오지 않았습니다."
    assert "평점" in restaurantText.text, "Error @restaurantInformation : 가게 정보 중 평점이 나오지 않았습니다."
    assert "전화번호" in restaurantText.text, "Error @restaurantInformation : 가게 정보 중 전화번호가 나오지 않았습니다."
    assert "주소" in restaurantText.text, "Error @restaurantInformation : 가게 정보 중 주소가 나오지 않았습니다."
    assert "오픈시간" in restaurantText.text, "Error @restaurantInformation : 가게 정보 중 오픈 시간이 나오지 않았습니다."
    assert "마감시간" in restaurantText.text, "Error @restaurantInformation : 가게 정보 중 마감시간이 나오지 않았습니다."
    assert "정보" in restaurantText.text, "Error @restaurantInformation : 가게 정보 중 정보가 나오지 않았습니다."
    
    restaurantMenu = driver.find_element_by_xpath("//div[@class='menu']")
    assert restaurantMenu.is_displayed(), "Error @restaurantInformation : 메뉴 정보가 나오지 않았습니다."

def restaurantLike(driver):
    
    driver.get("http://127.0.0.1:8000/login/")
    time.sleep(15)

    idBox = driver.find_element_by_xpath("//div[@class='login']/form/input[@name='userID']")
    assert idBox.is_displayed()
    idBox.clear()
    idBox.send_keys(customerID)
    
    pwBox = driver.find_element_by_xpath("//div[@class='login']/form/input[@name='password']")
    assert pwBox.is_displayed()
    pwBox.clear()
    pwBox.send_keys(customerPW)

    loginSubmit = driver.find_element_by_xpath("//input[@value='로그인']")
    loginSubmit.click()

    time.sleep(10)
    



    restaurantInformation(driver)
    time.sleep(20)
    
    likeIcon = driver.find_element_by_xpath("//div[@class='goodicon']/a/img[@class='icon']")
    assert likeIcon.is_displayed(), "Error @restaurantLike : 즐겨찾기 버튼이 표시되지 않았습니다."

    likeIcon.click()

    goodNum = driver.find_element_by_xpath("//div[@class='goodnum']")
    assert goodNum.is_displayed(), "Error @restaurantLike : 즐겨찾는 사람 수가 표시되지 않았습니다."
    likeIcon = driver.find_element_by_xpath("//div[@class='goodicon']/a/img[@class='icon']")
    likeIcon.click()

def writeReview(driver):

    review = "good"
    driver.get("http://127.0.0.1:8000/login/")
    time.sleep(15)

    idBox = driver.find_element_by_xpath("//div[@class='login']/form/input[@name='userID']")
    assert idBox.is_displayed()
    idBox.clear()
    idBox.send_keys(customerID)
    
    pwBox = driver.find_element_by_xpath("//div[@class='login']/form/input[@name='password']")
    assert pwBox.is_displayed()
    pwBox.clear()
    pwBox.send_keys(customerPW)

    loginSubmit = driver.find_element_by_xpath("//input[@value='로그인']")
    loginSubmit.click()

    time.sleep(10)
    



    restaurantInformation(driver)
    time.sleep(20)

    reviewTextArea = driver.find_element_by_xpath("//div[@id='REVIEW']/form/div[@id='register_review']/textarea")
    assert reviewTextArea.is_displayed(), "Error @writeReview : Review를 작성할 textarea가 표시되지 않았습니다."

    reviewTextArea.clear()
    reviewTextArea.send_keys(review)

    reviewSubmit = driver.find_element_by_xpath("//div[@id='register_review']/button")
    reviewSubmit.click()

    reviewContainer = driver.find_element_by_xpath("//div[@class='review_container']")
    assert reviewContainer.is_displayed(), "Error @writeReview : Review container가 표시되지 않았습니다."

    reviewSectionTitle = driver.find_element_by_xpath("//div[@class='review_container']/span[@class='review_section_title']")
    assert reviewSectionTitle.is_displayed(), "Error @writeReview : Review section Title이 표시되지 않았습니다."

    reviewComponentTitle = driver.find_element_by_xpath("//div[@class='review_component']/span[@class='review_name']")
    assert reviewComponentTitle.is_displayed(), "Error @writeReview : Review Component Title 이 표시되지 않았습니다."

    reviewComponentRating = driver.find_element_by_xpath("//div[@class='review_component']/span[@class='review_rating']")
    assert reviewComponentRating.is_displayed(), "Error @writeReview : Review Component Rating이 표시되지 않았습니다."

    reviewComponentComment = driver.find_element_by_xpath("//div[@class='review_component']/span[@class='review_comment']")
    assert reviewComponentComment.is_displayed(), "Error @writeReview : Review Component Comment가 표시되지 않았습니다."



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
    #search(driver)
    #clickCategoryImage(driver)
    #clickCategoryText(driver)
    #clickRestaurant(driver)
    #restaurantInformation(driver)
    #restaurantLike(driver)
    writeReview(driver)