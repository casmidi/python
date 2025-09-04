from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

# Buka halaman login
driver.get("https://www.saucedemo.com/")

# Isi username & password yang salah
driver.find_element(By.ID, "user-name").send_keys("salah_user")
driver.find_element(By.ID, "password").send_keys("salah_password")

# Klik login
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Cari pesan error
error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
print("Pesan error yang tampil:", error_message)

# Assertion: cek apakah pesan error sesuai harapan
assert "Username and password do not match" in error_message, "❌ Pesan error tidak sesuai!"

print("✅ Validasi login gagal berhasil.")

driver.quit()
