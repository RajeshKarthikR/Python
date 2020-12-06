from selenium import webdriver
import time
class application():

    def webpage(self):


        driver = webdriver.Chrome(executable_path="E:\\Rajesh\\Jar\\chromedriver.exe")
        driver.get("http://demo.automationtesting.in/Alerts.html")
        driver.maximize_window()
        alertpop = driver.find_element_by_xpath("//button[@class='btn btn-danger']")
        alertpop.click()
        driver.switch_to.alert.accept()
        time.sleep(30)
        print ("alert takencare")


page = application()
page.webpage()