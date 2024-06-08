from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

from selenium.webdriver.common.action_chains import ActionChains

#----------------------------------------------------------------------------------------------------------------
edge_options = EdgeOptions()
edge_driver_path= "C:/Users/RITIKA VERMA/Desktop/webdriver/msedgedriver.exe"
edge_driver = webdriver.Edge(executable_path=edge_driver_path)

#-----------------------------------------------------------------------------------------------------------------
#getting the ebay home page
edge_driver.get("https://www.ebay.com/")
#-----------------------------------------------------------------------------------------------------------------

#getting the register page
register_page = WebDriverWait(edge_driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="gh-ug-flex"]/a'))
)
register_page.click()
print("Clicked on the register page.")
#----------------------------------------------------------------------------------------------------------------
# Login Automate Function
def ebay_Login_automate_func(First_Name, Last_Name, EMAIL, PassWord, PhoneNum):

    #getting switched to personal aacount
    personal_account = WebDriverWait(edge_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContent"]/div[3]/div[2]/div[3]/div/div/div/label[1]'))
    )
    personal_account.click()
    print("Clicked on the personal_account.")
    #________________________________________________________________________________________________________________

    #Entering the First name
    firstName = WebDriverWait(edge_driver, 10).until(
            EC.visibility_of_element_located((By.ID, "firstname"))
        )
    firstName.send_keys(First_Name)
    #________________________________________________________________________________________________________________

    #Entering the Last Name 
    lastName = WebDriverWait(edge_driver, 10).until(
            EC.visibility_of_element_located((By.ID, "lastname"))
        )
    lastName.send_keys(Last_Name)
    #________________________________________________________________________________________________________________

    #Entering the Email address
    emailAdd =WebDriverWait(edge_driver, 10).until(
            EC.visibility_of_element_located((By.ID, "Email"))
        )
    emailAdd.send_keys(EMAIL)

    #________________________________________________________________________________________________________________

    #Entering the password 
    passcode =WebDriverWait(edge_driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
    passcode.send_keys(PassWord)
    #________________________________________________________________________________________________________________

    #submitting the signup page
    register_page = WebDriverWait(edge_driver, 10).until(
        EC.element_to_be_clickable((By.ID, "EMAIL_REG_FORM_SUBMIT"))
    )
    register_page.click()
    print("submitted the register page.")
    #________________________________________________________________________________________________________________

    # Entering the Phone Number Authentication
    phoneAuth = WebDriverWait(edge_driver, 20).until(
            EC.visibility_of_element_located((By.ID, "phoneCountry"))
        )
    phoneAuth.send_keys(PhoneNum)
    #________________________________________________________________________________________________________________

    # Submitting the Phone Number Authentication
    subPhoneAuth = WebDriverWait(edge_driver, 10).until(
        EC.element_to_be_clickable((By.ID, "SEND_AUTH_CODE"))
    )
    subPhoneAuth.click()
    print("submitted the phone number authentication.")
    #________________________________________________________________________________________________________________
    # User will receive OTP that has to be put mannualy, Then after authentication, account will be freshly created.
#-------------------------------------------------------------------------------------------------------------------
#ebay_Login_automate_func("XYZ", "ABC", "XYZ@gmail.com", "PQR@2002", 9999999999)
#-------------------------------------------------------------------------------------------------------------------