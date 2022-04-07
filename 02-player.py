# 01 test simple get of site pages
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

print(f'running test {2:2}')
print("the embedded player requires login")
username = input("username: ")
password = input("password: ")

# launch
driver = webdriver.Firefox()

# login
driver.get('https://zed.dev.reelradio.com/user/main.php')
driver.find_element(by=By.NAME, value='username').send_keys(username)
driver.find_element(by=By.NAME, value='password').send_keys(password)
driver.find_element(by=By.NAME, value='sublogin').click()
sleep(1)

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

