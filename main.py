from textformat import timeAndText
import time, config, functions as f, driver as d, actions as ma, stats as s

''' Gathering all requirements '''
driver = d.initalizeDriver()
randomWordList = f.getRandomWordList()

''' Login to microsoft and opening rewards '''
ma.loginToMicrosoft(driver)
ma.openRewardsPage(driver)

''' Bing search '''
ma.searchForWordList(driver, randomWordList)

''' Print current stats '''
#print(s.getAllStats(driver))

''' Ending script '''
timeAndText('Closing script')
driver.close()