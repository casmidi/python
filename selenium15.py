from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Hilangkan log DEPRECATED_ENDPOINT
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Jalankan Chrome
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

# Buka halaman login
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# --- Login ---
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# --- Add to cart backpack ---
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)

# --- Masuk ke cart ---
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

# --- Klik Checkout ---
driver.find_element(By.ID, "checkout").click()
time.sleep(2)

# --- Isi data checkout ---
driver.find_element(By.ID, "first-name").send_keys("Casmidi")
driver.find_element(By.ID, "last-name").send_keys("Asli")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()
time.sleep(2)

# --- Verifikasi ada item di checkout overview ---
items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
print("Item di checkout:", [item.text for item in items])

# --- Finish checkout ---
driver.find_element(By.ID, "finish").click()
time.sleep(2)

# --- Verifikasi sukses checkout ---
success_msg = driver.find_element(By.CLASS_NAME, "complete-header").text
print("Pesan setelah checkout:", success_msg)

# Tutup browser
time.sleep(3)
driver.quit()
