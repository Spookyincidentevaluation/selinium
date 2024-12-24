from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def main(context):
    # Start by logging the function start
    context.log("Starting the Selenium function...")

    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Disable sandbox (required for some environments)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Disable shared memory usage

    # Debug log to confirm options setup
    context.log("Chrome options set for headless mode: %s" % chrome_options.arguments)

    try:
        # Initialize the WebDriver (Chrome)
        context.log("Initializing Chrome WebDriver...")

        driver = webdriver.Chrome(options=chrome_options)

        # Debug log to confirm WebDriver initialization
        context.log("Chrome WebDriver initialized successfully.")
        
        # Open google.com
        context.log("Opening Google.com...")
        driver.get("https://www.google.com")
        
        # Wait for the page to load (you can adjust the sleep time if necessary)
        time.sleep(2)
        
        # Get the page title to confirm that the page is loaded
        page_title = driver.title
        context.log("Page title is: %s" % page_title)

        # Close the browser
        driver.quit()

        # Return a success response with the page title
        return context.res.json({"status": "Google opened successfully", "page_title": page_title})

    except Exception as e:
        # If an error occurs, log the error message
        context.error("Error: " + str(e))
        return context.res.json({"status": "Failed to open Google", "error": str(e)})
