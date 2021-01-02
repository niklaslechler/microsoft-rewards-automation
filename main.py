from textformat import timeAndText
import time, config, functions as f, driver as d, actions as ma, stats as s

''' Gathering all requirements '''
driver = d.initalizeDriver()
randomWordList = f.getRandomWordList()

''' Login to microsoft and opening rewards '''
ma.loginToMicrosoft(driver)
ma.openRewardsPage(driver)

''' Saving starting stats '''
f.writeLoginData(driver)

''' Bing search '''
#ma.searchForWordList(driver, randomWordList)

''' Ending script and saving new stats '''
f.closeScript(driver)