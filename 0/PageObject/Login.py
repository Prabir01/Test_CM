from time import sleep

from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver= driver
        self.emailid=(By.ID, "agentemail")
        self.password=(By.ID, "agentpassword")
        self.signin=(By.XPATH, "//button[@name='Submit']")


    def login(self,Environment_selection):
        environment_URL = Environment_selection

        if environment_URL == "QA":
            self.driver.get("https://qa-portal.blueleopard.com/login/bzi")
            self.driver.find_element(*self.emailid).send_keys("prabir.sahoo@xceedance.com")
            self.driver.find_element(*self.password).send_keys("Welcometohome@123")
        elif environment_URL == "UAT":
            self.driver.get("https://portal.uat.blueleopard.com/login/bzi")
            self.driver.find_element(*self.emailid).send_keys("prabir.sahoo@xceedance.com")
            self.driver.find_element(*self.password).send_keys("Welcometohome@1")

        sleep(2)
        self.driver.find_element(*self.signin).click()