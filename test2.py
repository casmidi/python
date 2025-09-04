from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Buka halaman login demo
driver.get("https://the-internet.herokuapp.com/login")

# Isi username & password
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Klik tombol login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(3)

# Ambil pesan sukses
message = driver.find_element(By.ID, "flash").text
print("Pesan login:", message)

driver.quit()
