#This tests the advanced search functionality in Chrome.
import sys, getopt
import wait
from time import sleep
from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

opts, args = getopt.getopt(sys.argv[1:], "d", ["debug"])

# launch
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
options = Options()
options.accept_insecure_certs = True
# check search page
driver.get('https://zed.dev.reelradio.com/search.php')
sleep(5)
search_input = driver.find_element(by=By.NAME, value='search_query')
search_input.send_keys('Tom Shannon' + Keys.ENTER)
wait(opts)

search_input.clear()
search_input.send_keys('Sacramento' + Keys.ENTER)
wait(opts)

search_input.clear()
search_input.send_keys('tina delgado' + Keys.ENTER)
wait(opts)

driver.find_element(by=By.NAME, value='search_query').clear()
driver.find_element(by=By.NAME, value='search_query').send_keys('' + Keys.ENTER)
wait(opts)

driver.quit()