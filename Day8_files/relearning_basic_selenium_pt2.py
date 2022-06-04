#
# Goal: Go to the orange County Craigslist Site, Find Expresso Machines for Sale
#
# install selenium: pip install selenium
# insall unidecode: pip install Unidecode
# if your on windows, make sure the chromedriver is in the same folder as this file
#
# 
# it helps to see how other people did the same thing: https://www.linkedin.com/pulse/automate-finding-items-craigslist-python-selenium-rescue-ravi-shankar/
#
#
#
#
#
# import the modeules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unidecode

# Use Chrome for hte Driver
driver = webdriver.Chrome()

# go the Orange County Craigslist Site
driver.get("https://orangecounty.craigslist.org/search/sssg")

# find the word craigslist in the browser title
assert "craigslist" in driver.title

# look at the source code of the search bar and try to find that element
# https://selenium-python.readthedocs.io/locating-elements.html
# we see in the source code of hte page that the id is "query"
elem = driver.find_element(By.ID, 'query')

# applies the clear method on the search bar
elem.clear()

# types in some word - you can run commands one at a time until it validates
# what you are tying to do
elem.send_keys("espresso machines")

# press enter
elem.send_keys(Keys.RETURN)

# if everything works correctly, you should see some espresso machines
# this says "find the word espresso in the source code of the web page"
assert "espresso" in driver.page_source

# documentation online mentions that it would be more useful if i was using the beautiful soup module - will do that for another day
# for now i will just find text and click on stuff


# Closes the window
driver.close()