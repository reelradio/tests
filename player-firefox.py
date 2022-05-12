# 01 test simple get of site pages
import sys, getopt
from getpass import getpass
import wait
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

opts, args = getopt.getopt(sys.argv[1:], "d", ["debug"])

print("Running test " + sys.argv[0])

print("the embedded player requires login")
username = input("username: ")
password = getpass()

# launch
driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

# login
driver.get('https://zed.dev.reelradio.com/user/main.php')
driver.find_element(by=By.NAME, value='username').send_keys(username)
driver.find_element(by=By.NAME, value='password').send_keys(password)
wait.pause(opts)
driver.find_element(by=By.NAME, value='sublogin').click()
sleep(1)

# load the embedded player
driver.get('https://zed.dev.reelradio.com/ram/embedded_player.html')
sleep(1)

# switch to iframe
iframe = driver.find_element(by=By.ID, value='reel-content')
driver.switch_to.frame(iframe)
wait.pause(opts)

# navigate to a collection and start an exhibit
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='COLLECTIONS').click()
wait.pause(opts)
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='David Adams').click()
wait.pause(opts)
driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Tom Shannon, WKBW Buffalo').click()
wait.pause(opts)

# done
driver.quit()

