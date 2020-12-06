from selenium import webdriver
import time

class login():

    def newlogin(self):

        driver = webdriver.Chrome(executable_path="E:\\Rajesh\\Jar\\chromedriver.exe")
        driver.get("https://www.szonline.in/")
        driver.maximize_window()
        Login = driver.find_element_by_xpath("//span[text()='Login']").click()
        Mobile = driver.find_element_by_id("mobile").send_keys(8123435916)
        password = driver.find_element_by_id("pass").send_keys("Qwer@1234")
        click = driver.find_element_by_name("send").click()
        time.sleep(15)
        driver.__getattribute__()
new = login()
new.newlogin()

