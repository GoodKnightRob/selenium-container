from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

# sleep(5)

# driver = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

# driver.get('https://python.org')
# driver.save_screenshot('screenshot.png')


from fastapi import FastAPI

# creates an api object
app = FastAPI()

@app.get("/")
def home():
    sleep(5)

    # Using Firefox with Selenium Hub
    options = webdriver.FirefoxOptions()
    driver = webdriver.Remote(command_executor='http://selenium-hub:4444/wd/hub',options=options)
    driver.get('https://google.com')
    driver.save_screenshot('google.png')
    return {"Data":"Test"}