from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Tentukan lokasi ChromeDriver
service = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Buka Google
driver.get("https://www.google.com")

# Tampilkan judul halaman
print("Judul halaman:", driver.title)

# Cari kotak pencarian
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("QA Automation")
search_box.submit()

# Tunggu sebentar biar hasil terlihat
time.sleep(5)

# Tutup browser
driver.quit()
