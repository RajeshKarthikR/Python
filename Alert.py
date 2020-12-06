from selenium import webdriver
import time
class application():

    def webpage(self):


        driver = webdriver.Chrome(executable_path="E:\\Rajesh\\Jar\\chromedriver.exe")
        driver.get("http://demo.automationtesting.in/Alerts.html")
        driver.maximize_window()
        alertpop = driver.find_element_by_xpath("//a [text() ='Alert with Textbox ']")
        alertpop.click()

        clickbutton = driver.find_element_by_xpath("//button[text() ='click the button to demonstrate the prompt box ']")
        clickbutton.click()

        alert_one = driver.switch_to.alert
        alert_one.send_keys("Hi")
        alert_one.accept()

        time.sleep(30)
        print("alert takencare")

page = application()
page.webpage()