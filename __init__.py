import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Get destination path from "config.json"
with open("config.json", "r") as file:
    data = json.load(file)
destination_path = data["path"]

os.environ["WDM_LOCAL"] = destination_path

# Install new version
webdriver_path = ChromeDriverManager().install()
# Check version and save in variable.
driver = webdriver.Chrome(service=Service(webdriver_path))
version = driver.capabilities["chrome"]["chromedriverVersion"].split(" ")[0]


# Move file to destination path.
# shutil.move(webdriver_path, destination_path)

print(f"ChromeDriver has been updated to version {version}")

driver.quit()
