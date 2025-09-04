from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Hilangkan pesan log ChromeDriver
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Buat driver
driver = webdriver.Chrome(options=chrome_options)

# Buka halaman demo login
driver.get("https://the-internet.herokuapp.com/login")

# Cari field username dan password
username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

# Isi form
username_field.send_keys("myUsername")
password_field.send_keys("myPassword123")

# Biar bisa dilihat sebentar sebelum quit
time.sleep(3)

driver.quit()
