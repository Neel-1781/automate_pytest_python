import pytest
from selenium import webdriver
import os

def test_browserstack():
    # 1. Get credentials from Jenkins environment variables
    username = os.environ.get('BROWSERSTACK_USERNAME')
    access_key = os.environ.get('BROWSERSTACK_ACCESS_KEY')

    # 2. Check if credentials exist
    if not username or not access_key:
        pytest.fail("BrowserStack credentials not found in environment variables")

    # 3. Configure capabilities (What browser to use)
    caps = {
        'os': 'Windows',
        'os_version': '10',
        'browser': 'Chrome',
        'browser_version': 'latest',
        'name': 'Jenkins Python 3.6 Test',
        'build': 'Jenkins Build',
        'bstack:options': {
            'accessibility': True
    }

    # 4. Construct the BrowserStack URL
    bstack_url = 'https://' + username + ':' + access_key + '@hub-cloud.browserstack.com/wd/hub'

    # 5. Initialize Driver manually
    driver = webdriver.Remote(
        command_executor=bstack_url,
        desired_capabilities=caps
    )

    # 6. Run Test
    try:
        driver.get("https://bstackdemo.com")
        print("Page Title: " + driver.title)
        assert "StackDemo" in driver.title
    finally:
        # 7. Always quit the driver
        driver.quit()
