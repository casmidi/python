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

# Tunggu sebentar
time.sleep(2)

# --- Login ---
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# --- Klik Add to Cart untuk item pertama ---
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(2)

# --- Cek cart badge (jumlah item di keranjang) ---
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
print("Jumlah item di cart:", cart_badge)

# Tutup browser setelah selesai
time.sleep(3)
driver.quit()
