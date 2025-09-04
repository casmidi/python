from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

# Buka halaman login di saucedemo
driver.get("https://www.saucedemo.com/")

# Cari field username dan password
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")

# Isi form
username_field.send_keys("standard_user")
password_field.send_keys("secret_sauce")

time.sleep(3)
driver.quit()
