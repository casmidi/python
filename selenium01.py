from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\\chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")

print("Judul halaman:", driver.title)

driver.quit()
