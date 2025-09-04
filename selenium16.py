from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Hilangkan warning DEPRECATED_ENDPOINT
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Jalankan Chrome
service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

# Data login (username, password)
login_data = [
    ("standard_user", "secret_sauce"),   # valid
    ("locked_out_user", "secret_sauce"), # user terkunci
    ("standard_user", "salah_password"), # password salah
    ("", "secret_sauce"),                # username kosong
    ("standard_user", ""),               # password kosong
]

for username, password in login_data:
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    # Masukkan username & password
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Cek apakah login berhasil atau gagal
    try:
        # Jika ada menu burger, berarti login sukses
        driver.find_element(By.ID, "react-burger-menu-btn")
        print(f"[SUCCESS] Login berhasil dengan user='{username}' password='{password}'")
    except:
        # Kalau gagal, ambil pesan error
        try:
            error_msg = driver.find_element(By.CLASS_NAME, "error-message-container").text
            print(f"[FAILED] Login gagal dengan user='{username}' password='{password}' | Pesan: {error_msg}")
        except:
            print(f"[FAILED] Login gagal dengan user='{username}' password='{password}' | Pesan: Tidak diketahui")

time.sleep(2)
driver.quit()
