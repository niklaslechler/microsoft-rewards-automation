from selenium.webdriver.common.keys import Keys
from textformat import timeAndText
import time, config, functions as f
import driver as d

email = config.email
password = config.password

''' Gathering all requirements '''
driver = d.initalizeDriver()
randomWordList = f.getRandomWordList()

''' Login to microsoft '''


''' Ending script '''
driver.close()