# 01 test simple get of site pages
from time import sleep
from selenium import webdriver

print(f'running test {1:2}')

# launch
driver = webdriver.Firefox()

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

