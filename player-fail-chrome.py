# 01 test simple get of site pages
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# launch
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

# load the embedded player
driver.get('https://zed.dev.reelradio.com/ram/embedded_player.html')
sleep(1)

# switch to iframe
iframe = driver.find_element(by=By.ID, value='reel-content')
driver.switch_to.frame(iframe)
sleep(1)

# navigate to a collection and start an exhibit
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='COLLECTIONS').click()
sleep(1)
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='David Adams').click()
sleep(1)
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Tom Shannon, WKBW Buffalo').click()
sleep(5)

# done
driver.quit()

