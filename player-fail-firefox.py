# 01 test simple get of site pages
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

# launch
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

# load the embedded player
driver.get('https://zed.dev.reelradio.com/ram/embedded_player.html')
sleep(1)

# switch to iframe
iframe = driver.find_element(by=By.ID, value='reel-content')
driver.switch_to.frame(iframe)
input("press enter to continue")

# navigate to a collection and start an exhibit
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='COLLECTIONS').click()
input("press enter to continue")
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='David Adams').click()
input("press enter to continue")
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Tom Shannon, WKBW Buffalo').click()
input("press enter to continue")

# done
driver.quit()

