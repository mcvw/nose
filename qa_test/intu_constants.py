# Title : intu Digital QA Test
# Author: Michael Walden
# File  : intu_constants.py
# Date  : 26Jun2017

# Description: This file contains contstants used by intu Digital QA Test

BROWSER_CHROME = "Chrome"
BROWSER_FIREFOX = "Firefox"
DEFAULT_WAIT_DURATION = 30

HOME_PAGE_URL = "http://intu.co.uk/signup"
HOME_PAGE_TITLE = "Sign up"

FIRST_NAME = "Eric"
SURNAME = "Barney"
EMAIL = "barney_walden@hotmail.com"
DD = "6"
MM = "9"
YYYY = "2001"
GENDER = "M"

SUBMIT_BUTTON = "(//button[@type='submit'])[2]"

SUCCESS_ELEMENT = "#successMessage > p"
SUCCESS_TEXT = u"You’ve been added to our mailing list. Look out for exciting intu offers and updates soon."
FAILURE_ELEMENT = "#failureMessage > p"
FAILURE_TEXT = "Apologies, we have been unable to submit your details, please try again."
FIRST_NAME_ELEMENT = "small.error"
FIRST_NAME_TEXT = "Please enter your first name"
SURNAME_ELEMENT = "div.columns.error > small.error"
SURNAME_TEXT = "Please enter your surname"
EMAIL_ELEMENT = "div.columns.error > small.error"
EMAIL_TEXT = "Please enter your email address"
DOB_ELEMENT = "div.columns > div.error > small.error"
DOB_TEXT = "Please enter your date of birth"
GENDER_ELEMENT = "div.columns.error > small.error"
GENDER_TEXT = "Please enter your gender"