import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Argument parser for handling flags
parser = argparse.ArgumentParser(description='Time tracking automation')
parser.add_argument('--pause', action='store_true', help='Pause for breakfast')
parser.add_argument('--resume', action='store_true', help='Resume workday')
args = parser.parse_args()

chrome_options = Options()
chrome_options.add_argument("--headless")  
service = Service('./chromedriver')

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://auth2.bixpe.com/Account/Login")

    username_input = driver.find_element(By.NAME, "Username")
    password_input = driver.find_element(By.NAME, "Password")

    username = os.getenv("BIXPE_USERNAME")
    password = os.getenv("BIXPE_PASSWORD")
    print(f"Username: {username}")
    print(f"Password: {password}")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    time.sleep(2)

    if args.pause:
        pause_button = driver.find_element(By.ID, "btn-pause-breakfast")
        pause_button.click()
        print("Breakfast pause activated.")

        time.sleep(2)
        
        text_input = driver.find_element(By.CSS_SELECTOR, "input.swal2-input")
        text_input.send_keys("food")
        
        confirm_button = driver.find_element(By.CLASS_NAME, "swal2-confirm")
        confirm_button.click()

    elif args.resume:
        resume_button = driver.find_element(By.ID, "btn-resume-workday")
        resume_button.click()
        print("Workday resumed.")
        
    else:
        register_button = driver.find_element(By.ID, "btn-stop-workday")
        if register_button.value_of_css_property("display") == "none":
            register_button = driver.find_element(By.ID, "btn-start-workday")

        register_button.click()
        time.sleep(2)
        
        confirm_button = driver.find_element(By.CLASS_NAME, "swal2-confirm")
        confirm_button.click()

        print("Time tracking completed.")

except Exception as e:
    print(f"Automation error: {e}")
finally:
    driver.quit()
