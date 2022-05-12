# 01 test simple get of site pages
import sys, getopt
from getpass import getpass
from time import sleep
import wait
from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

opts, args = getopt.getopt(sys.argv[1:], "d", ["debug"])

print("Running test " + sys.argv[0])

print("the embedded player requires login")
username = input("username: ")
password = getpass()
# launch
driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))

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
wait.pause(opts, wait=10)

#wait the exhibit, then replay it
driver.switch_to.default_content()
driver.execute_script("document.querySelector('#audioplayer').pause();")
wait.pause(opts, 5)
driver.execute_script("document.querySelector('#audioplayer').play();")
wait.pause(opts, 5)

#Change/mute volume
driver.execute_script("document.querySelector('#audioplayer').volume = 0.5;")
wait.pause(opts, 5)
driver.execute_script("document.querySelector('#audioplayer').volume = 0;")
wait.pause(opts, 5)
driver.execute_script("document.querySelector('#audioplayer').volume = 0.2;")
wait.pause(opts, 5)
#Seek to a specific time
driver.execute_script("document.querySelector('#audioplayer').currentTime = 60;")
wait.pause(opts, 5)
driver.execute_script("document.querySelector('#audioplayer').currentTime = 1200;")
wait.pause(opts, 5)
driver.execute_script("document.querySelector('#audioplayer').pause();")

# done
driver.quit()