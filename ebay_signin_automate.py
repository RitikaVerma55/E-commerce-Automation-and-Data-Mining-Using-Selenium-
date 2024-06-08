from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.edge.service import Service
import time
import sys
from selenium.webdriver.common.action_chains import ActionChains

#----------------------------------------------------------------------------------------------

edge_options = EdgeOptions()
edge_driver_path= "C:/Users/RITIKA VERMA/Desktop/webdriver/msedgedriver.exe"
edge_driver = webdriver.Edge(executable_path=edge_driver_path)
#----------------------------------------------------------------------------------------------

#getting the ebay home page
edge_driver.get("https://www.ebay.com/")
#---------------------------------------------------------------------------------------------

#getting the sign-up page
sign_up = WebDriverWait(edge_driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/header/div[1]/ul[1]/li[1]/span/a'))
)
sign_up.click()
print("Clicked on the sign-up page.")
#----------------------------------------------------------------------------------------------

#Entering the userID
UserID =WebDriverWait(edge_driver, 10).until(
        EC.visibility_of_element_located((By.ID, "userid"))
    )
UserID.send_keys("vermaritika2015@gmail.com")
#----------------------------------------------------------------------------------------------

#Clicking on Continue 
continue_signup = WebDriverWait(edge_driver, 10).until(
    EC.element_to_be_clickable((By.ID, "signin-continue-btn"))
)
continue_signup.click()
print("submitted the sign-up page.")

#Error Handling (If account doesn't exists)
try:
    error_message = WebDriverWait(edge_driver, 10).until(
        EC.presence_of_element_located((By.ID, "signin-error-msg")) 
    )
    print(error_message.text)
    if error_message.text == "We couldn't find this eBay account.":
        flag =0

        print("Account doesn't exist. Clicking on Login...")

        create_acc = WebDriverWait(edge_driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="create-account-link"]' ))
        )
        create_acc.click()
        flag=1
        if flag==1:
            print(flag)
            def ebay_sign_automate_func(First_Name, Last_Name, EMAIL, PassWord, PhoneNum):

                #getting switched to personal aacount
                personal_account = WebDriverWait(edge_driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'segmentActive'))
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

            ebay_sign_automate_func("jiya", "Gaikwrad", "vermaritika2015@gmail.com", "ritikA@2015", 9871536561)
        
    else:
        print("okay report")
        
except TimeoutException:
    print("Account exists (no error message within 10 seconds).")

#----------------------------------------------------------------------------------------------
# Entering the password
pass_word =WebDriverWait(edge_driver, 10).until(
        EC.visibility_of_element_located((By.ID, "pass"))
    )
#Entering the wrong password
#pass_word.send_keys("ritika@2015")
#Entering the right password
pass_word.send_keys("ritikA@2015")
#-----------------------------------------------------------------------------------------------
#APPROACH 1
#Clicking to complete SIgnIN 
complete_signup = WebDriverWait(edge_driver, 10).until(
    EC.element_to_be_clickable((By.ID, "sgnBt"))
)
complete_signup.click()
print("submitted the complete sign-up page.")

# Error Handling
try:
    pass_error_message = WebDriverWait(edge_driver, 5).until(
        EC.presence_of_element_located((By.ID, "errormsg")) 
    )
    print(pass_error_message.text)
    if pass_error_message =="Oops, that s not a match.":
        print("Incorrect password is entered.")
        sys.exit()

except:
    print("No error, Successfully Signed In.")
#------------------------------------------------------------------------------------------------
#APPROACH 2 
#Clicking to complete SIgnIN 
complete_signup = WebDriverWait(edge_driver, 10).until(
    EC.element_to_be_clickable((By.ID, "sgnBt"))
)
complete_signup.click()
print("submitted the complete sign-up page.")

# Error Handling
try:
    pass_error_message = WebDriverWait(edge_driver, 5).until(
        EC.presence_of_element_located((By.ID, "errormsg")) 
    )
    print(pass_error_message.text)
    if pass_error_message =="Oops, that s not a match.":
        print("Incorrect password is entered.")
        
        change_password = WebDriverWait(edge_driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="psi__container-r3 psi__container--needhelp"]/a'))
        )
        change_password.click()

        Receive_Email_button = WebDriverWait(edge_driver, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn btn--fluid btn--truncated btn--primary"))
        )
        Receive_Email_button.click()
        #OTP on registered EmailID has to be manually
        # A Successful change is password is then done. Now, Can signin with the new password.

except:
    print("No error, Successfully Signed In.")


#-------------------------------------------------------------------------------------------------
#Add Continue Button:
skip_button = WebDriverWait(edge_driver, 5).until(
    EC.element_to_be_clickable((By.ID, "passkeys-cancel-btn"))
)
skip_button.click()
print("Completed Signup. Home page is Visible.")
#------------------------------------------------------------------------------------------------

