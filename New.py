from selenium import webdriver

class application():

    def webpage(self):


        driver = webdriver.Chrome(executable_path="E:\\Rajesh\\Jar\\chromedriver.exe")
        driver.get("http://demo.automationtesting.in/Register.html")
        driver.maximize_window()
        CheckLastName = driver.find_element_by_xpath("//input[@placeholder='Last Name']")
        CheckLastName.is_enabled()
        CheckLastName.send_keys("Karthik")

        Hobbies = driver.find_element_by_id("checkbox1")
        Hobbies.click()
        if Hobbies.is_selected():
            print("you have selected cricket")



page = application()
page.webpage()

