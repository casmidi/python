from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

# Buka halaman login
driver.get("https://www.saucedemo.com/")

# Isi username & password
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Klik login
driver.find_element(By.ID, "login-button").click()
time.sleep(3)

# Assertion: cek apakah URL mengandung "/inventory.html"
current_url = driver.current_url
print("URL setelah login:", current_url)

assert "/inventory.html" in current_url, "Login gagal! Tidak masuk ke halaman inventory."

print("✅ Login berhasil dan berada di halaman Inventory.")

driver.quit()
