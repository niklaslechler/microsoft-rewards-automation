from selenium.webdriver.common.keys import Keys
from textformat import timeAndText
import time, config, functions as f, driver as d, actions as ma

''' Gathering all requirements '''
driver = d.initalizeDriver()
randomWordList = f.getRandomWordList()

''' Login to microsoft '''
ma.loginToMicrosoft(driver, config.email, config.password)

''' Ending script '''
driver.close()