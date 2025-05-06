from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Endorsement:
    def __init__(self,driver):
        self.driver=driver

    def endorsement_VerifyEndorsementInitiate(self):
        self.driver.find_element(By.XPATH, "//a[text()='Endorse']").click()
        self.driver.find_element(By.XPATH, "//input[@id='endeffectivedate']").send_keys("05/05/2025")
        self.driver.find_element(By.XPATH, "//button[text()='Next']").click()
        sleep(5)

    def endorsement_VerifyQuoteCreation(self):
        commissionpageloading = WebDriverWait(self.driver, 30)
        commissionpageloading.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='COMMISSION']")))
        self.driver.find_element(By.XPATH, "//a[text()='COMMISSION']").click()
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-check']").click()
    def endorsement_VerifyQuoteSummary(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[text()='Insured Name :']")))
        endquoteNumber = self.driver.find_element(By.XPATH, "(//h3[@class='qoutno word-break-all padding-left-18'])[1]").text
        print(endquoteNumber)
        #sleep(2)
    def endorsement_VerifyEndorsementBind(self):
        self.driver.execute_script("window.scrollBy(0,50);")
        self.driver.find_element(By.XPATH, "//span[text()='Buy Now']").click()
        #sleep(2)
        wait2 = WebDriverWait(self.driver, 30)
        wait2.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h3[@class='qoutno word-break-all']")))
        ENPolicyNumber = self.driver.find_element(By.XPATH, "//h3[@class='qoutno word-break-all']").text
        print(ENPolicyNumber)
        sleep(5)