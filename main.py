from textformat import timeAndText
import time, config, functions as f, driver as d, actions as ma

''' Gathering all requirements '''
driver = d.initalizeDriver()
randomWordList = f.getRandomWordList()
print(randomWordList)

''' Login to microsoft and opening rewards '''
ma.loginToMicrosoft(driver)
ma.openRewardsPage(driver)

''' Bing search '''
ma.searchForWordList(driver, randomWordList)

''' Ending script '''
timeAndText('Closing script')
driver.close()