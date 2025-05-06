from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.Login import LoginPage
from PageObject.CM_NewBusiness import CM_NBQuestionSet
from PageObject.CM_Endorsement import Endorsement
from PageObject.CM_Cancel import CM_Cancel


def test_commmotor(browserinstance,Environment_selection):
    sleep(5)
    #browser invocation
    driver = browserinstance
    #environment_URL=Environment_selection
    #driver.get(environment_URL)
    #driver.get("https://qa-portal.blueleopard.com/login/bzi")
    driver.maximize_window()
    #Login
    loginpage= LoginPage(driver)
    loginpage.login(Environment_selection)
    sleep(10)

    #NBcreate Quote
    CM_NewBusiness=CM_NBQuestionSet(driver)
    CM_NewBusiness.commmotorcreatequote()
    #NBQuoteSummary
    CM_NewBusiness.NB_Quote_summary_verifyQuoteNumber()
    CM_NewBusiness.NB_Quote_summary_VerifyQuoteSummaryAndDocumentEmail()
    CM_NewBusiness.BuyNow()
    sleep(10)
    #NB PolicySummary
    CM_NewBusiness.NB_PolicySummaryVerifyPolicyNumber()
    # NB Policy Doc send
    CM_NewBusiness.NB_PolicySummary_verifyDocEmail()

    #Endorsement
    endorsement= Endorsement(driver)
    endorsement.endorsement_VerifyEndorsementInitiate()
    endorsement.endorsement_VerifyQuoteCreation()
    endorsement.endorsement_VerifyQuoteSummary()
    endorsement.endorsement_VerifyEndorsementBind()

    #Cancellation
    cancellation= CM_Cancel(driver)
    cancellation.cancel_VerifyCancellationInitiate()
    cancellation.cancel_VerifyCancellationReason()
    cancellation.cancel_VerifyCreateCancellationQuote()
    cancellation.cancel_VerifyConfirmCancellation()



