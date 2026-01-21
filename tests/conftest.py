import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="function")
def driver():
    # 1. Get credentials from Jenkins
    username = os.environ.get('BROWSERSTACK_USERNAME')
    access_key = os.environ.get('BROWSERSTACK_ACCESS_KEY')

    # 2. Configure capabilities
    caps = {
        'os': 'Windows',
        'os_version': '10',
        'browser': 'Chrome',
        'browser_version': 'latest',
        'name': 'Jenkins Sample Test',
        'build': 'Jenkins Build Python 3.6'
        'bstack:options': {
            'accessibility': true
    }
    }

    # 3. Connect to BrowserStack
    bstack_url = 'https://' + username + ':' + access_key + '@hub-cloud.browserstack.com/wd/hub'
    
    driver = webdriver.Remote(
        command_executor=bstack_url,
        desired_capabilities=caps
    )

    # 4. Pass the driver to the test, then quit when done
    yield driver
    driver.quit()
