#coding = utf-8
#Version:python3.6.0
import selenium
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")


if __name__ == '__main__':
    test_selenium()