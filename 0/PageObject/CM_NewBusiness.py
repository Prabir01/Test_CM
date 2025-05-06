from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class CM_NBQuestionSet:
    def __init__(self,driver):
        self.driver=driver
        self.new_Quote=(By.XPATH,"//ul[@class='navbar-nav mr-auto cs-navigation']/li[2]/a[text()=' New Quote ']")
        self.productselection=(By.XPATH,"//input[@id='svg_9']")
        self.submitproduct=(By.XPATH, "//button[@type='submit']")
        self.insuredname=(By.XPATH, "//input[@id='control_1.1']")
        self.Address=(By.XPATH, "//input[@id='control_1.4']")
        self.primaryBusinessActivity=(By.XPATH, '//input[@id="control_1.5"]')
        self.Next=(By.XPATH, "//div[@class='col-md-12 pull-right pt-3 text-right']/a[2]")

    def commmotorcreatequote(self):
        #Click on New Quote
        self.driver.find_element(*self.new_Quote).click()
        #Select product
        self.driver.find_element(*self.productselection).click()
        #Submit on NB screen
        self.driver.find_element(*self.submitproduct).click()
        #sleep(2)
        #Insured Name
        self.driver.find_element(*self.insuredname).send_keys("Prabir Test")
        self.driver.find_element(*self.Address).send_keys("14 CONN STREET, BRIGHTON QLD")
        #primaryBusinessActivitySelection=(By.XPATH, '//ngb-highlight[@class="ng-star-inserted"]')
        # Address search
        #sleep(2)
        addresses = self.driver.find_elements(By.XPATH, "//button[@role='option']")
        for address in addresses:
            if address.text == "14 CONN STREET, BRIGHTON QLD 4017":
                address.click()
                break
        #sleep(2)
        #primaryBusinessActivity
        self.driver.find_element(*self.primaryBusinessActivity).send_keys("Coffee/Tea Manufacturing")
        sleep(2)
        print(self.driver.find_element(By.XPATH, "//input[@id='control_1.5']").get_attribute("value"))
        # primaryBusinessActivitySelection
        #self.driver.find_element(*self.primaryBusinessActivitySelection).click()
        #sleep(2)
        # Primary Business Activity *
        activities = self.driver.find_elements(By.XPATH, "//ngb-highlight[@class='ng-star-inserted']")
        for activity in activities:
            if activity.text == "Coffee/Tea Manufacturing":
                activity.click()
        #sleep(2)
        # Next on Business Detail Page
        self.driver.find_element(*self.Next).click()

        # Next on UW criteria
        self.driver.find_element(*self.Next).click()

        # Vehicle Class *
        vehicleClass1 = Select(self.driver.find_element(By.XPATH, "//select[@id='0_control_3.16.1']"))
        vehicleClass1.select_by_index(0)

        # Cover Type *
        cover = Select(self.driver.find_element(By.XPATH, "//select[@id='0_control_3.16.3']"))
        cover.select_by_index(0)

        #sleep(2)
        # State of Vehicle Registration *
        state = Select(self.driver.find_element(By.XPATH, "//select[@formcontrolname='stateOfVehicleRegistration']"))
        state.select_by_index(7)
        #sleep(2)
        # Enter Rego Number
        self.driver.find_element(By.XPATH, "//input[@formcontrolname='registrationNumber']").send_keys("Dodgy7")
        #sleep(2)
        # Click on Search-(//input[@checked="val.Checked"])[1]
        self.driver.find_element(By.XPATH, "(//i[@class='fa fa-search'])[3]").click()
        #sleep(2)

        IsVehcileSelected = WebDriverWait(self.driver, 45)
        #IsVehcileSelected.until(EC.presence_of_element_located((By.XPATH, "//select[@formcontrolname='size']")))
        IsVehcileSelected.until(EC.visibility_of_element_located(
            (By.XPATH,"//label[text()='DB SERIES III, 4D SEDAN, MULTI POINT F/INJ, 3.8L, ES, 5 SP AUTO SPORTS MOD']")))
        # Sum Insured Type *
        dropdown = Select(self.driver.find_element(By.ID, "0_control_3.16.11"))
        dropdown.select_by_index(0)
        #sleep(2)
        # Street Address search and select
        self.driver.find_element(By.XPATH, "//input[@title='Street Address']").send_keys("14 conn")
        #sleep(5)
        addresses = self.driver.find_elements(By.XPATH, "//button[@class='dropdown-item ng-star-inserted']")
        for address in addresses:
            if address.text == "14 CONN STREET, BRIGHTON QLD 4017":
                print(address.text)
                address.click()
                break

        # Primary vehicle usage *
        primaryVehicleUsages = Select(self.driver.find_element(By.ID, "0_control_3.16.15"))
        primaryVehicleUsages.select_by_index(0)
        #sleep(2)

        # Is the vehicle used for any of the following *
        self.driver.find_element(By.XPATH, "(//label[normalize-space()='None of the above'])[1]").click()
        # supplied by the manufacturer?
        self.driver.find_element(By.XPATH, "//label[@for='0_3.16.17_NO']").click()
        # attachments or non-standard accessories?
        self.driver.find_element(By.XPATH, "//label[@for='0_3.16.18_NO']").click()
        # bodywork, paintwork or interior?
        self.driver.find_element(By.XPATH, "//label[@for='0_3.16.20_NO']").click()
        # other problems which make it unsafe to drive?
        self.driver.find_element(By.XPATH, "//label[@for='0_3.16.21_NO']").click()

        # Main driver year of birth *
        self.driver.find_element(By.ID, "0_control_3.16.35").send_keys("1990")
        # under 25 years old?
        self.driver.find_element(By.XPATH, "//label[@for='0_3.16.36_NO']").click()
        # Hire Car Extension?
        self.driver.find_element(By.XPATH, "//label[@for='0_3.16.37_NO']").click()
        # Excess Extension?
        self.driver.find_element(By.XPATH, "//label[@for='0_3.16.38_NO']").click()
        # Roadside Assist Extension?
        self.driver.find_element(By.XPATH, "//label[@for='0_3.16.39_NO']").click()

        # interested parties?
        self.driver.find_element(By.XPATH, "//label[@for='0_3.16.40_NO']").click()
        sleep(2)
        # # Adding additional vehicle.
        # driver.find_element(By.XPATH, "//i[@class='fa fa-plus-circle']").click()
        # sleep(2)
        # Vehcile2 = Select(driver.find_element(By.XPATH, "(//select[@id='1_control_3.16.1'])[1]"))
        # Vehcile2.select_by_index(1)
        #
        # # Cover Type of vehicle 2 *
        # cover2 = Select(driver.find_element(By.XPATH, "//select[@id='1_control_3.16.3']"))
        # cover2.select_by_index(1)
        #
        # # state of vehicle 2
        # StateofvehicleRegistration2 = Select(driver.find_element(By.ID, "1_control_3.16.5"))
        # StateofvehicleRegistration2.select_by_index(0)
        #
        # # Select Year of Manufacture for vehicle 2
        # driver.find_element(By.ID, "1_control_3.16.7").send_keys("1990")
        # # Make of Vehicle 2
        # driver.find_element(By.ID, "1_control_3.16.8").send_keys("Test_Make")
        # # VehicleDescription of vehicle 2
        # driver.find_element(By.ID, "1_control_3.16.9").send_keys("Test_VehicleDescription")
        #
        # # Sum insured
        # driver.find_element(By.ID, "1_control_3.16.12").send_keys("1000")
        #
        # # Address of V2
        # driver.find_element(By.XPATH, "//input[@formcontrolname='StreetAddress']").send_keys("1 KARL COURT")
        # address_vehicle2 = driver.find_elements(By.XPATH, "//ngb-highlight[@class='ng-star-inserted']")
        # for address_v2 in address_vehicle2:
        #     if address_v2.text == "1 KARL COURT, BUNDOORA VIC 3083":
        #         print(address_v2.text)
        #         address_v2.click()
        #         break
        #
        # # primaryVehicleUsages of v2
        # primaryVehicleUsages2 = Select(driver.find_element(By.ID, "1_control_3.16.15"))
        # primaryVehicleUsages2.select_by_index(0)
        # # Is the vehicle used for any of the following V2
        # driver.find_element(By.XPATH, "//label[@for='1_3.16.16_None']").click()
        #
        # # vehicle have any rust, hail V2
        # driver.find_element(By.XPATH, "//label[@for='1_3.16.20_NO']").click()
        #
        # # vehicle have any mechanical V2
        # driver.find_element(By.XPATH, "//label[@for='1_3.16.21_NO']").click()
        #
        # # vehicle garaged overnight  V2
        # vehicle_garaged_overnight = Select(driver.find_element(By.ID, '1_control_3.16.22'))
        # vehicle_garaged_overnight.select_by_index(0)
        #
        # # vehicle built with EPS V2
        # driver.find_element(By.XPATH, "//label[@for='1_3.16.24_NO']").click()
        #
        # # business conduct any V2
        # driver.find_element(By.XPATH, "//label[@for='1_3.16.25_None']").click()
        #
        # # ehicle/trailer fitted with both fire extinguisher V2
        # driver.find_element(By.XPATH, "//label[@for='1_3.16.30_NO']").click()
        #
        # # Main driver year of birth
        # driver.find_element(By.ID, "1_control_3.16.35").send_keys("1990")
        #
        # # driver under 25 year
        # driver.find_element(By.XPATH, "//label[@for='1_3.16.36_NO']").click()
        #
        # # interested parties V2
        # driver.find_element(By.XPATH, "//label[@for='1_3.16.40_NO']").click()

        # Next on schedule page
        self.driver.find_element(By.XPATH, "(//a[@class='btn btn-primary btn-next ng-star-inserted'])[2]").click()
        #sleep(5)

        self.driver.execute_script("window.scrollBy(0,1000);")
        self.driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
        #sleep(2)

    def NB_Quote_summary_verifyQuoteNumber(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Insured Name :']")))
        quoteNumber = self.driver.find_element(By.XPATH,
                                               "(//h3[@class='qoutno word-break-all padding-left-18'])[1]").text
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
        #sleep(2)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def BuyNow(self):
        self.driver.find_element(By.ID, "btnBuyNow").click()
        # Confirm buyNow
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-secondary btn-auto']").click()
    def NB_PolicySummaryVerifyPolicyNumber(self):
        NBPolicyNumber3 = self.driver.find_element(By.XPATH, "//h3[@class='qoutno word-break-all']").text
        print(NBPolicyNumber3)
    def NB_PolicySummary_verifyDocEmail(self):
        self.driver.find_element(By.XPATH, "//button[text()='Email']").click()
        self.driver.find_element(By.XPATH, "//button[text()='Send Email']").click()
        NBPolicyDocMail = WebDriverWait(self.driver, 15)
        NBPolicyDocMail.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Ok']")))
        self.driver.find_element(By.XPATH, "//button[text()='Ok']").click()