from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class NB_Quote_summary:
    def __init__(self,driver):
        self.driver=driver

    def NB_Quote_summary_verifyQuoteNumber(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Insured Name :']")))
        quoteNumber = self.driver.find_element(By.XPATH, "(//h3[@class='qoutno word-break-all padding-left-18'])[1]").text
        print(quoteNumber)

        # document sent
    def NB_Quote_summary_VerifyQuoteSummaryAndDocumentEmail(self):
        self.driver.find_element(By.XPATH, "//a[@id='one-tab']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Email']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Send Email']").click()
        NBQuoteDocMail = WebDriverWait(self.driver, 15)
        NBQuoteDocMail.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Ok']")))
        self.driver.find_element(By.XPATH, "//button[text()='Ok']").click()

        self.driver.find_element(By.XPATH,
                            "//button[@class='btn btn-primary font14 width-3dot55em ng-star-inserted']").click()
        # PolicyCondition after NEXT
        self.driver.find_element(By.XPATH, "(//button[@type='button'])[4]").click()
        # Client detail
        self.driver.find_element(By.XPATH, "//label[@for='clientDetailsNo']").click()
        sleep(2)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def BuyNow(self):
        self.driver.find_element(By.ID, "btnBuyNow").click()
        # Confirm buyNow
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-secondary btn-auto']").click()
