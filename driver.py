from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from textformat import timeAndText

# If True -> Browser won't be displayed
optionHeadless = False

def initalizeDriver():
    timeAndText('Initalizing driver')
    options = webdriver.ChromeOptions()
    options.headless = optionHeadless
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    timeAndText('Driver initalized successfully')
    return driver