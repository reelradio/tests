#This tests the advanced search functionality in Chrome.

from time import sleep
from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# launch
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
options = Options()
options.accept_insecure_certs = True
# check search page
driver.get('https://zed.dev.reelradio.com/search.php')
sleep(5)
search_input = driver.find_element(by=By.NAME, value='search_query')
search_input.send_keys('Tom Shannon' + Keys.ENTER)
sleep(5)

search_input.clear()
search_input.send_keys('Sacramento' + Keys.ENTER)
sleep(5)

search_input.clear()
search_input.send_keys('tina delgado' + Keys.ENTER)
sleep(5)

driver.quit()