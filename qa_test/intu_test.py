# Title : intu Digital QA Test
# Author: Michael Walden
# File  : intu_test.py
# Date  : 26Jun2017

'''
# Description: Task 4.
    For the test cases written in task 3, write the corresponding automated tests.
    Use http://intu.co.uk/signup as a base URL.
    Please use Selenium with PHP/Python.
'''

from nose import with_setup # optional
from nose.plugins.attrib import attr

# General imports
from selenium import webdriver
import time, re, sys, random

# imports required for the assignment
import intu_constants as ac
import intu_functions as af


def setup_module(module):
    print ("") # this is to get a newline after the dots
    print ("setup_module before anything in this file")

def teardown_module(module):
    print ("teardown_module after everything in this file")

def my_setup_function():
    print ("my_setup_function")

def my_teardown_function():
    print ("my_teardown_function")

''' TestTask4
Scenario: Unit test cases as per Task3
'''
class TestTask4:
    def setup(self):
        print ("TestTask4: setup() before each test method")
        
        # Set browser flavour
        print("\t\t-- Set browser instance:", self._browser_instance)
        if self._browser_instance == ac.BROWSER_CHROME:
            self._driver = webdriver.Chrome()
        elif self._browser_instance == ac.BROWSER_FIREFOX:
            self._driver = webdriver.Firefox()

        # Set driver attributes
        self._driver.implicitly_wait(ac.DEFAULT_WAIT_DURATION)
        self.accept_next_alert = True
        self._driver.maximize_window()
        self._driver.delete_all_cookies()

        # Open URL
        url = ""
        af.open_url(self, url, ac.HOME_PAGE_TITLE) 
        #time.sleep(5)

    def teardown(self):
        print ("TestTask4: teardown() after each test method")

    @classmethod
    def setup_class(self):
        print ("setup_class() before any methods in this class")
        self._driver = None
        self._verification_errors = []
        self._base_url = ac.HOME_PAGE_URL
        self._browser_instance = ac.BROWSER_CHROME
        self._email_value = random.randint(1000,1000000)
        
    @classmethod
    def teardown_class(self):
        print ("teardown_class() after any methods in this class")

    #######################################################################################################################

    ''' MT0
    Scenario: Verify that Sign up page used for all subsequent tests is accessible and that the expected elements are visible and enabled
        Given that the URL displays the correct page
        When all fields are enabled and visible
        Then proceed to subsequent test
    '''
    @attr(priority='1')
    def test_mt0(self):
        print("\n\t--> INTU MT0 Start")
        errorText = ""

        try:
            af.set_first_name(self)
            af.set_surname(self)
            af.set_email(self)
            af.set_date_of_birth(self)
            af.set_gender(self)

        except Exception as e:
            errorText = "MT0: " + str(e)
            self._verification_errors.append(errorText)
            raise e.with_traceback(sys.exc_info()[2])

        time.sleep(5)
        print("\t<-- INTU MT0 END")

        assert errorText == ""

    ''' MT1
    Scenario: Submit values representing a new account
        Given all fields are valid
        And the email address is NOT already registered
        When the submit button is clicked
        Then display success message
    '''
    @attr(priority='2')
    def test_mt1(self):
        print("\n\t--> INTU MT1 Start")
        errorText = ""

        try:
            af.set_first_name(self, ac.FIRST_NAME)
            af.set_surname(self, ac.SURNAME)
            af.set_email(self, str(self._email_value) + ac.EMAIL)
            af.set_date_of_birth(self, ac.DD, ac.MM, ac.YYYY)
            af.set_gender(self, ac.GENDER)
            af.submit(self)
            af.check_message(self, ac.SUCCESS_ELEMENT, ac.SUCCESS_TEXT)

        except Exception as e:
            errorText = "MT1: " + str(e)
            self._verification_errors.append(errorText)
            raise e.with_traceback(sys.exc_info()[2])

        time.sleep(5)
        print("\t<-- INTU MT1 END")

        #self.assertEqual(u"You’ve been added to our mailing list. Look out for exciting intu offers and updates soon.", #driver.find_element_by_css_selector("#successMessage > p").text)
        assert errorText == ""

    ''' MT2
    Scenario: Submit values representing an existing account
        Given all fields are valid
        And the email address is already registered
        When the submit button is clicked
        Then display error message
    '''
    @attr(priority='2')
    def test_mt2(self):
        print("\n\t--> INTU MT2 Start")
        errorText = ""

        try:
            af.set_first_name(self, ac.FIRST_NAME)
            af.set_surname(self, ac.SURNAME)
            af.set_email(self, str(self._email_value) + ac.EMAIL)
            af.set_date_of_birth(self, ac.DD, ac.MM, ac.YYYY)
            af.set_gender(self, ac.GENDER)
            af.submit(self)
            af.check_message(self, ac.FAILURE_ELEMENT, ac.FAILURE_TEXT)
            
        except Exception as e:
            errorText = "MT2: " + str(e)
            self._verification_errors.append(errorText)
            raise e.with_traceback(sys.exc_info()[2])

        time.sleep(5)
        print("\t<-- INTU MT2 END")

        assert errorText == ""

    ''' MT3
    Scenario: Submit values where value for First name field is null
        Given all other fields are valid
        When the value for first name is null
        Then display error message
    '''
    @attr(priority='3')
    def test_mt3(self):
        print("\n\t--> INTU MT3 Start")
        errorText = ""

        try:
            af.set_first_name(self)
            af.set_surname(self, ac.SURNAME)
            af.set_email(self, str(self._email_value) + ac.EMAIL)
            af.set_date_of_birth(self, ac.DD, ac.MM, ac.YYYY)
            af.set_gender(self, ac.GENDER)
            af.submit(self)
            af.check_message(self, ac.FIRST_NAME_ELEMENT, ac.FIRST_NAME_TEXT)

        except Exception as e:
            errorText = "MT3: " + str(e)
            self._verification_errors.append(errorText)
            raise e.with_traceback(sys.exc_info()[2])

        time.sleep(5)
        print("\t<-- INTU MT3 END")

        assert errorText == ""

    ''' MT4
    Scenario: Submit values where value for Surname field is null
        Given all other fields are valid
        When the value for surname is null
        Then display error message
    '''
    @attr(priority='3')
    def test_mt4(self):
        print("\n\t--> INTU MT4 Start")
        errorText = ""

        try:
            af.set_first_name(self, ac.FIRST_NAME)
            af.set_surname(self)
            af.set_email(self, str(self._email_value) + ac.EMAIL)
            af.set_date_of_birth(self, ac.DD, ac.MM, ac.YYYY)
            af.set_gender(self, ac.GENDER)
            af.submit(self)
            af.check_message(self, ac.SURNAME_ELEMENT, ac.SURNAME_TEXT)

        except Exception as e:
            errorText = "MT4: " + str(e)
            self._verification_errors.append(errorText)
            raise e.with_traceback(sys.exc_info()[2])

        time.sleep(5)
        print("\t<-- INTU MT4 END")

        assert errorText == ""

    ''' MT5
    Scenario: Submit values where value for Email field is null
        Given all other fields are valid
        When the value for email is null
        Then display error message
    '''
    @attr(priority='3')
    def test_mt5(self):
        print("\n\t--> INTU MT5 Start")
        errorText = ""

        try:
            af.set_first_name(self, ac.FIRST_NAME)
            af.set_surname(self, ac.SURNAME)
            af.set_email(self)
            af.set_date_of_birth(self, ac.DD, ac.MM, ac.YYYY)
            af.set_gender(self, ac.GENDER)
            af.submit(self)
            af.check_message(self, ac.EMAIL_ELEMENT, ac.EMAIL_TEXT)

        except Exception as e:
            errorText = "MT5: " + str(e)
            self._verification_errors.append(errorText)
            raise e.with_traceback(sys.exc_info()[2])

        time.sleep(5)
        print("\t<-- INTU MT5 END")

        assert errorText == ""

    ''' MT6
    Scenario: Submit values where value components for Date of birth field are not selected
        Given all other fields are valid
        When any of the date of birth fields are not selected
        Then display error message
    '''
    @attr(priority='3')
    def test_mt6(self):
        print("\n\t--> INTU MT6 Start")
        errorText = ""

        try:
            af.set_first_name(self, ac.FIRST_NAME)
            af.set_surname(self, ac.SURNAME)
            af.set_email(self, str(self._email_value) + ac.EMAIL)
            af.set_date_of_birth(self, "", ac.MM, ac.YYYY)
            af.set_gender(self, ac.GENDER)
            af.submit(self)
            af.check_message(self, ac.DOB_ELEMENT, ac.DOB_TEXT)
            
        except Exception as e:
            errorText = "MT6: " + str(e)
            self._verification_errors.append(errorText)
            raise e.with_traceback(sys.exc_info()[2])

        time.sleep(5)
        print("\t<-- INTU MT6 END")

        assert errorText == ""

    ''' MT7
    Scenario: Submit values where value for Gender is not selected
        Given all other fields are valid
        When Gender is not selected
        Then display error message
    '''
    @attr(priority='3')
    def test_mt7(self):
        print("\n\t--> INTU MT7 Start")
        errorText = ""

        try:
            af.set_first_name(self, ac.FIRST_NAME)
            af.set_surname(self, ac.SURNAME)
            af.set_email(self, str(self._email_value) + ac.EMAIL)
            af.set_date_of_birth(self, ac.DD, ac.MM, ac.YYYY)
            af.set_gender(self)
            af.submit(self)
            af.check_message(self, ac.GENDER_ELEMENT, ac.GENDER_TEXT)

        except Exception as e:
            errorText = "MT7: " + str(e)
            self._verification_errors.append(errorText)
            raise e.with_traceback(sys.exc_info()[2])

        time.sleep(5)
        print("\t<-- INTU MT7 END")

        assert errorText == ""