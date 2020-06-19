from django.test import TestCase
from selenium import webdriver
import time

# Create your tests here.

if __name__ == '__main__':
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    driver.get('http://127.0.0.1:8000/')

    time.sleep(10)

    driver.close()