from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time

# List of URLs to capture
urls = [
    "https://example.com",
    "https://www.wikipedia.org",
    "https://www.python.org",
    "https://weather.com/weather/radar/interactive/l/6063c8e183412a8992ef0122babe9d05bb76d9c5e95993c1ca8f57064f16b56d",
    "https://weather.com/weather/tenday/l/6063c8e183412a8992ef0122babe9d05bb76d9c5e95993c1ca8f57064f16b56d"
]

# Directory to save screenshots
output_dir = "screenshots"
os.makedirs(output_dir, exist_ok=True)

# Configure Selenium with Chrome in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")

# Path to your chromedriver executable
chromedriver_path = r"C:\Users\Robbo\PycharmProjects\repository\selenium\chromedriver-win64\chromedriver.exe"  # <-- UPDATE THIS PATH
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Capture screenshots
for url in urls:
    try:
        driver.get(url)
        time.sleep(4)  # wait for the page to fully load

        # Clean filename from URL
        filename = url.replace("https://", "").replace("http://", "").replace("/", "_")
        filepath = os.path.join(output_dir, f"{filename}.png")

        driver.save_screenshot(filepath)
        print(f"Captured: {url} -> {filepath}")
    except Exception as e:
        print(f"Error capturing {url}: {e}")

# Clean up
driver.quit()