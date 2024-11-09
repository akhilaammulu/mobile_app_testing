import requests

# API URL and expired API key
api_url = "https://api.example.com/data"
expired_api_key = "expired_api_key_here"

# Function to test API status and key validity
def test_api():
    response = requests.get(api_url, headers={"Authorization": f"Bearer {expired_api_key}"})
    
    if response.status_code == 401:
        print("Error: API Key is expired!")
        return False
    elif response.status_code == 200:
        print("API request successful")
        return True
    else:
        print(f"Unexpected response: {response.status_code}")
        return False

# Run the test
test_api()
