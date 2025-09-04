# lesson04_widgets.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, tempfile, time

service = Service(r"C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

try:
    # Dropdown
    driver.get("https://the-internet.herokuapp.com/dropdown")
    Select(wait.until(EC.element_to_be_clickable((By.ID, "dropdown")))).select_by_visible_text("Option 2")

    # Checkbox
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    cbs = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    if not cbs[0].is_selected():
        cbs[0].click()

    # Alerts
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    driver.switch_to.alert.accept()

    # iFrame
    driver.get("https://the-internet.herokuapp.com/iframe")
    driver.switch_to.frame("mce_0_ifr")
    editor = driver.find_element(By.ID, "tinymce")
    editor.clear(); editor.send_keys("Hello from Selenium!")
    driver.switch_to.default_content()

    # New window
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    main, new = driver.window_handles
    driver.switch_to.window(new)
    print("Window title (new):", driver.title)
    driver.close()
    driver.switch_to.window(main)

    # Upload file
    driver.get("https://the-internet.herokuapp.com/upload")
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as f:
        f.write(b"Selenium upload test"); temp_path = f.name
    driver.find_element(By.ID, "file-upload").send_keys(temp_path)
    driver.find_element(By.ID, "file-submit").click()
    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h3"), "File Uploaded!"))
    print("✅ Upload OK:", os.path.basename(temp_path))
finally:
    driver.quit()
    try:
        os.remove(temp_path)
    except Exception:
        pass
