from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from textformat import timeAndText
import time, config as c

# Check how to remove error messages
def initalizeDriver():
    timeAndText('Initalizing driver')
    options = webdriver.ChromeOptions()
    if c.optionHeadless: options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    timeAndText('Driver initalized successfully')
    return driver

def openPage(driver, url: str, pageName=None):
    if pageName is not None: timeAndText('Opening {} page'.format(pageName))
    driver.get(url)
    time.sleep(3)