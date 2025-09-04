from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Hilangkan pesan log ChromeDriver
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Buat driver
driver = webdriver.Chrome(options=chrome_options)

# Buka halaman demo login
driver.get("https://the-internet.herokuapp.com/login")

# Ambil teks dari elemen h2
header = driver.find_element(By.TAG_NAME, "h2")
print("Judul halaman:", driver.title)
print("Isi h2:", header.text)

driver.quit()
