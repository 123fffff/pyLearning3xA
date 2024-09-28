import time

from selenium import webdriver
def test_practice():
    driver=webdriver.chrome()
    driver.get("https://awesomeqa.com/practice.html")

    time.sleep(5)
    driver.quit()

