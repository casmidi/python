from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Buka browser (Chrome)
driver = webdriver.Chrome()

# 2. Arahkan ke halaman login demo
driver.get("https://the-internet.herokuapp.com/login")

# 3. Cari input username (dengan ID = 'username') lalu ketikkan teks
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")  # contoh username

# 4. Cari input password (dengan ID = 'password') lalu ketikkan teks
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")  # contoh password

# 5. Tunggu 3 detik biar kita bisa lihat prosesnya
time.sleep(3)

# 6. Tutup browser
driver.quit()
