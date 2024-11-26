import time
from os import makedirs
from os.path import exists
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import requests
import yaml

DIR_NAME = yaml.safe_load(open('config.yaml', 'r')).get('dir_param')
SLEEP_TIME =  yaml.safe_load(open('config.yaml', 'r')).get('time_param')
LINK1 = yaml.safe_load(open('config.yaml', 'r')).get('browser_params').get('link_1')
LINK2 = yaml.safe_load(open('config.yaml', 'r')).get('browser_params').get('link_2')
USERNAME = yaml.safe_load(open('config.yaml', 'r')).get('login_params').get('username')
PASSWORD = yaml.safe_load(open('config.yaml', 'r')).get('login_params').get('password')

if not exists(DIR_NAME):
    makedirs(DIR_NAME)

browser = webdriver.Chrome(service = Service(), options = webdriver.ChromeOptions())
browser.get('https://www.linkedin.com/login')
file = open('config.txt')
lines = file.readlines()

elementID = browser.find_element(By.ID,'username')
elementID.send_keys(USERNAME)

elementID = browser.find_element(By.ID, 'password')
elementID.send_keys(PASSWORD)

elementID.submit()

time.sleep(SLEEP_TIME)

browser.get(LINK1)

img1_element = browser.find_element(By.XPATH, "//img[@width='200']")
# img1_element = browser.find_element(By.CLASS_NAME, "evi-image") #if it's your own profile you can use this too
img1_src =  img1_element.get_attribute("src")

time.sleep(SLEEP_TIME)

browser.get(LINK2)

img2_element = browser.find_element(By.XPATH, "//img[@width='200']")
img2_src = img2_element.get_attribute("src")

browser.close()

# Saving Images
img1 = Image.open(requests.get(img1_src, stream=True).raw)
img1.save('data/image1.jpg')

img2 = Image.open(requests.get(img2_src, stream=True).raw)
img2.save('data/image2.jpg')

#the background.jpg I searched in the Google and save by myself :)
