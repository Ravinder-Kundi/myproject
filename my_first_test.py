import time
from selenium import webdriver

website = input()
driver = webdriver.Chrome(executable_path="C://Users//rubyk//pythonProject//resources//chromedriver.exe")
driver.maximize_window()
driver.get("http://" + website)
