from appium import webdriver
import time
import requests

# Sample API check for expired key
api_url = "https://api.example.com/data"
expired_api_key = "expired_api_key_here"

# Perform API check before running mobile tests
response = requests.get(api_url, headers={"Authorization": f"Bearer {expired_api_key}"})
if response.status_code == 401:
    print("Error: API Key is expired! Exiting tests.")
    exit()  # Stop tests if API key is expired

# Define the desired capabilities for Android or iOS
desired_caps = {
    "platformName": "Android",  # Use "iOS" for iOS
    "platformVersion": "10",  # Change version as needed
    "deviceName": "Android Emulator",  # Use actual device name for testing
    "appPackage": "com.example.android",  # Replace with your app's package name
    "appActivity": "com.example.android.MainActivity",  # Replace with app's main activity
    "automationName": "UiAutomator2",  # Use "XCUITest" for iOS
}

# Initialize Appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Test: Verify app launch
time.sleep(5)
assert driver.current_activity != ".MainActivity", "App did not launch correctly."

# Perform some UI interactions (e.g., clicking a button)
button = driver.find_element_by_id("com.example.android:id/button")
button.click()

# Add more UI checks here

# End the Appium session
driver.quit()
