# This tests the advanced search functionality in Firefox.
import sys, getopt
import wait
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

opts, args = getopt.getopt(sys.argv[1:], "d", ["debug"])

# launch
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

# check search page
driver.get('https://zed.dev.reelradio.com/search.php')
driver.find_element(by=By.NAME, value='search_query').send_keys('Tom Shannon' + Keys.ENTER)
wait(opts)

driver.find_element(by=By.NAME, value='search_query').clear()
driver.find_element(by=By.NAME, value='search_query').send_keys('Sacramento' + Keys.ENTER)
wait(opts)

driver.find_element(by=By.NAME, value='search_query').clear()
driver.find_element(by=By.NAME, value='search_query').send_keys('tina delgado' + Keys.ENTER)
wait(opts)

driver.find_element(by=By.NAME, value='search_query').clear()
driver.find_element(by=By.NAME, value='search_query').send_keys('' + Keys.ENTER)
wait(opts)

driver.quit()