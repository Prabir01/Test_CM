from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CM_Cancel:
    def __init__(self,driver):
        self.driver=driver

    def cancel_VerifyCancellationInitiate(self):
        self.driver.find_element(By.XPATH, "//a[text()='Cancel']").click()
    def cancel_VerifyCancellationReason(self):
        CancellationReason = Select(self.driver.find_element(By.XPATH, "//select[@id='CancellationReason']"))
        CancellationReason.select_by_visible_text("Processing error")
    def cancel_VerifyCreateCancellationQuote(self):
        self.driver.find_element(By.XPATH, "//button[text()='Submit']").click()
        CanQuoteSummary = WebDriverWait(self.driver, 20)
        CanQuoteSummary.until(
            expected_conditions.presence_of_element_located((By.XPATH, "(//h3[@class='qoutno word-break-all padding-left-18'])[1]")))
        canquoteNumber = self.driver.find_element(By.XPATH, "(//h3[@class='qoutno word-break-all padding-left-18'])[1]").text
        sleep(3)
        print(canquoteNumber)
    def cancel_VerifyConfirmCancellation(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, "//a[text()=' Confirm Cancellation']").click()
        self.driver.get_screenshot_as_file("screenshot.png")
        CancelPolicy = self.driver.find_element(By.XPATH, "//h3[@class='qoutno word-break-all']").text
        print(CancelPolicy)
        sleep(5)
