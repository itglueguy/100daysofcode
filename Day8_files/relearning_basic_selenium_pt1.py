#
# Goal: Just get it doing something; the next one will allow us to do something more custom
#
# install selenium: pip install selenium
# if your on windows, make sure the chromedriver is in the same folder as this file
# import the modeules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Use Chrome for hte Driver
driver = webdriver.Chrome()

# go the python website
driver.get("http://www.python.org")

# find the word Python in the browser title
assert "Python" in driver.title

# This elemenent seems to relate to the search bar
elem = driver.find_element(By.NAME, "q")

# applies the clear method on the search bar
elem.clear()

# types in some word
elem.send_keys("toni bot was here")

# press enter
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

# Closes the window
driver.close()