from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class application():

    def webpage(self):

        driver = webdriver.Chrome(executable_path="E:\\Rajesh\\Jar\\chromedriver.exe")
        baseurl = ("http://demo.automationtesting.in/Datepicker.html")
        driver.maximize_window()
        driver.get(baseurl)
#
        driver.find_element_by_xpath("//input [@id='datepicker2']").send_keys("11/26/2020",Keys.ENTER)

        time.sleep(30)


page = application()
page.webpage()