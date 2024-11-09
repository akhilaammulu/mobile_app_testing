#!/bin/bash

# Set up a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the tests
python test_api.py
python test_appium.py

# Generate the Allure report
pytest --alluredir=allure-results
allure serve allure-results

# Clean up
deactivate
