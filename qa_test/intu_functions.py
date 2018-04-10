# Title : intu Digital QA Test
# Author: Michael Walden
# File  : intu_functions.py
# Date  : 26Jun2017

# Description: This file contains functions used by intu Digital QA Test

# General imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, re, sys

# imports required for the assignment
import intu_constants as ac


'''
Open URL
'''
def open_url(self, url, urlTitle):
    print("\n\t\t--> open_url START")
    try:
        print("\t\t\t-- Goto URL:", self._base_url + url)
        # Open browser instance using base URL
        self._driver.get(self._base_url + url)
        assert(urlTitle == self._driver.title)
        
        print("\t\t\t-- Verified page:", urlTitle)
    
    except Exception as e:
        self._verification_errors.append("open_url:" + str(e))
        raise e.with_traceback(sys.exc_info()[2])

    print("\t\t<-- open_url END") 

'''
Set First Name
'''
def set_first_name(self, firstName = "NULL"):
    print("\n\t\t--> set_first_name START")

    try:
        element = self._driver.find_element_by_name("first_name")
        if element is not None:
            element.click()
        
        if firstName is not "NULL":
            element.clear()
            element.send_keys(firstName)
        
        print("\t\t\t-- set_first_name successful")
    
    except Exception as e:
        self._verification_errors.append("set_first_name:" + str(e))
        raise e.with_traceback(sys.exc_info()[2])

    print("\t\t<-- set_first_name END")

'''
Set Surname
'''
def set_surname(self, surname = "NULL"):
    print("\n\t\t--> set_surname START")

    try:
        element = self._driver.find_element_by_name("surname")
        if element is not None:
            element.click()
        
        if surname is not "NULL":
            element.clear()
            element.send_keys(surname)
        
        print("\t\t\t-- set_surname successful")
    
    except Exception as e:
        self._verification_errors.append("set_surname:" + str(e))
        raise e.with_traceback(sys.exc_info()[2])

    print("\t\t<-- set_surname END")

'''
Set Email
'''
def set_email(self, email = "NULL"):
    print("\n\t\t--> set_email START")

    try:
        element = self._driver.find_element_by_id("email")
        if element is not None:
            element.click()

        if email is not "NULL":
            element.clear()
            element.send_keys(email)
        
        print("\t\t\t-- set_email successful")
    
    except Exception as e:
        self._verification_errors.append("set_email:" + str(e))
        raise e.with_traceback(sys.exc_info()[2])

    print("\t\t<-- set_email END")

'''
Set Date of Birth
'''
def set_date_of_birth(self, dd = "", mm = "", yyyy = ""):
    print("\n\t\t--> set_date_of_birth START")

    try:
        element = self._driver.find_element_by_id("dd")
        if element is not None:
            element.click()
        
        element.send_keys(dd)

        element = self._driver.find_element_by_id("mm")
        if element is not None:
            #element.click()
            print("Do nothing for mm")
        
        element.send_keys(mm)

        element = self._driver.find_element_by_id("yyyy")
        if element is not None:
            #element.click()
            print("Do nothing for yyyy")
        
        element.send_keys(yyyy)

        print("\t\t\t-- set_date_of_birth successful")
    
    except Exception as e:
        self._verification_errors.append("set_date_of_birth:" + str(e))
        raise e.with_traceback(sys.exc_info()[2])

    print("\t\t<-- set_date_of_birth END")
                  
'''
Set Gender
'''
def set_gender(self, gender = ""):
    print("\n\t\t--> set_gender START")

    try:
        element = self._driver.find_element_by_id("gender")
        if element is not None:
            element.click()

        element.send_keys(gender)

        print("\t\t\t-- set_gender successful")

    except Exception as e:
        self._verification_errors.append("select_gender:" + str(e))
        raise e.with_traceback(sys.exc_info()[2])

    print("\t\t<-- set_gender END")

'''
Submit
'''
def submit(self, xpathString = ac.SUBMIT_BUTTON):
    print("\n\t\t--> submit START")

    try:
        element = self._driver.find_element_by_xpath(xpathString)
        if element is not None:
            element.click()
                
        print("\t\t\t-- submit successful")

    except Exception as e:
        self._verification_errors.append("submit:" + str(e))
        raise e.with_traceback(sys.exc_info()[2])

    print("\t\t<-- submit END")
    time.sleep(5)

'''
Check message
'''
def check_message(self, message, messageText):
    print("\n\t\t--> check_message START")
    
    try:
        element = self._driver.find_element_by_css_selector(message)
        element2 = self._driver.find_element(By.CSS_SELECTOR, message)
        print("e: ", element.text)
        print("e2: ",element2.text)
        if element is not None:
            assert element.text == messageText
            
        print("\t\t\t-- found message")

    except Exception as e:
        self._verification_errors.append("check_message:" + str(e))
        raise e.with_traceback(sys.exc_info()[2])

    print("\t\t<-- check_message END")