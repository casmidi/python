from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

# Step 1: Buka halaman login
driver.get("https://www.saucedemo.com/")

# Step 2: Login dengan akun valid
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Step 3: Klik tombol "Add to cart" untuk produk pertama (Sauce Labs Backpack)
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)

# Step 4: Ambil teks jumlah keranjang
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
print("Jumlah item di keranjang:", cart_badge)

# Step 5: Assertion jumlah item = 1
assert cart_badge == "1", "❌ Barang gagal masuk ke keranjang!"

print("✅ Barang berhasil ditambahkan ke keranjang.")

driver.quit()
