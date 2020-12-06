from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class application():

    def webpage(self):

        driver = webdriver.Chrome(executable_path="E:\\Rajesh\\Jar\\chromedriver.exe")
        baseurl = ("http://demo.automationtesting.in/Frames.html")
        driver.maximize_window()
        driver.get(baseurl)
        frameone = driver.switch_to.frame(driver.find_element_by_xpath("//a[@href='#Single']"))
    
        textValue = driver.find_element_by_xpath("//div//input[@type='text']")




        time.sleep(10)


page = application()
page.webpage()