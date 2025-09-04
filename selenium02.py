from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Lokasi ChromeDriver
service = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# 1. Buka halaman web
driver.get("https://the-internet.herokuapp.com/login")

# 2. Print judul halaman
print("Judul halaman:", driver.title)

# 3. Print URL aktif
print("URL aktif:", driver.current_url)

# 4. Tutup browser
driver.quit()
