from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Lokasi ChromeDriver
service = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 1. Buka halaman login
driver.get("https://the-internet.herokuapp.com/login")

# 2. Isi username
driver.find_element(By.ID, "username").send_keys("tomsmith")

# 3. Isi password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# 4. Klik tombol login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)  # biar hasilnya terlihat

# 5. Ambil pesan hasil login
message = driver.find_element(By.ID, "flash").text
print("Pesan hasil login:", message)

# 6. Tutup browser
driver.quit()
