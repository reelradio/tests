# This tests the advanced search functionality in Firefox.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# launch
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

# check search page
driver.get('https://zed.dev.reelradio.com/search.php')
driver.find_element(by=By.NAME, value='search_query').send_keys('Tom Shannon' + Keys.ENTER)
sleep(5)

driver.find_element(by=By.NAME, value='search_query').clear()
driver.find_element(by=By.NAME, value='search_query').send_keys('Sacramento' + Keys.ENTER)
sleep(5)

driver.find_element(by=By.NAME, value='search_query').clear()
driver.find_element(by=By.NAME, value='search_query').send_keys('tina delgado' + Keys.ENTER)
sleep(5)

driver.quit()