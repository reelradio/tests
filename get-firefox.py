# 01 test simple get of site pages
from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

print(f'running test {1:2}')

# launch
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

# get main site
driver.get('https://zed.dev.reelradio.com')
sleep(1)

# check embedded player page
driver.get('https://zed.dev.reelradio.com/ram/embedded_player.html')
sleep(1)

# check search page
driver.get('https://zed.dev.reelradio.com/search.php')
sleep(1)

driver.quit()

