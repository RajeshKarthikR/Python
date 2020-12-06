from selenium import webdriver

class launch():

    def newlink(self):

        driver = webdriver.Chrome(executable_path="E:\\Rajesh\\Jar\\chromedriver.exe")
        driver.get("https://www.szonline.in/")
        driver.maximize_window()
        Register = driver.find_element_by_xpath("//span[text()='Register']")
        Register.click()
        Firstname = driver.find_element_by_name("firstname")
        Firstname.send_keys("Raj")
        Lastname = driver.find_element_by_name("lastname").send_keys("R")
        Email = driver.find_element_by_name("email").send_keys("rameshrajesh1@yahoo.com")
        Mobile = driver.find_element_by_name("mobile").send_keys(8123435916)
        password = driver.find_element_by_name("password").send_keys("Qwer@1234")
        confirmpassword = driver.find_element_by_name("confirmation").send_keys("Qwer@1234")
        Signup = driver.find_element_by_name("is_subscribed")
        Signup.click()
        Finalregister = driver.find_element_by_xpath("//button[@title='Register']").click()



page = launch()
page.newlink()