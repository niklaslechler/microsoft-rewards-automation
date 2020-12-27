from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time, config, functions as f

email = config.email
password = config.password

''' Initalize driver '''
options = webdriver.ChromeOptions()
# options.headless = True -> Browser won't be displayed
options.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

''' Create random word list '''
#randomWordList = f.getRandomWordList()

''' Login to microsoft '''


''' Close driver '''
driver.close()