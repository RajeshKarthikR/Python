from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class application():

    def webpage(self):

        driver = webdriver.Chrome(executable_path="E:\\Rajesh\\Jar\\chromedriver.exe")
        baseurl = ("http://demo.automationtesting.in/Static.html")
        driver.maximize_window()
        driver.get(baseurl)
        drag = driver.find_element_by_xpath("//div//img[@src='logo.png']")
        drop = driver.find_element_by_xpath("//div[@id='droparea']")

        time.sleep(10)

page = application()
page.webpage()