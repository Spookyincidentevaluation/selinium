from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

def main(context):
    context.log("Starting the function...")

    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        # Start Chrome WebDriver
        context.log("Initializing Chrome WebDriver...")
        driver = webdriver.Chrome(options=chrome_options)
        context.log("Chrome WebDriver initialized successfully.")
        
        # Open google.com
        driver.get("https://www.google.com")
        context.log("Navigating to Google...")

        # Let the page load for a moment
        time.sleep(2)

        # Log the page title to confirm the page has loaded
        context.log("Page title is: " + driver.title)

        # Close the browser
        driver.quit()

        # Return a simple response to confirm the function worked
        return context.res.json({"status": "Google opened successfully"})
    
    except Exception as e:
        context.error("Error: " + str(e))
        return context.res.json({"status": "Failed to open Google", "error": str(e)})
