''' Actions on the microsoft/bing page '''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from textformat import timeAndText
import functions as f
import driver as d
import config as c
import time

# Check if login was successfull
def loginToMicrosoft(driver):
    timeAndText('Logging in to microsoft account')
    d.openPage(driver, 'https://login.live.com/login.srf')
    time.sleep(3)
    driver.find_element_by_name('loginfmt').send_keys(c.email)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input').click()
    time.sleep(3)
    driver.find_element_by_name('passwd').send_keys(c.password)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input').click()
    time.sleep(3)
    timeAndText('Login successfull')

def openRewardsPage(driver):
    timeAndText('Opening Microsoft Rewards page')
    d.openPage(driver, 'https://account.microsoft.com/rewards')

def singleSearchBing(driver, searchEntry):
    d.openPage(driver, 'https://www.bing.com/search?q={}'.format(searchEntry))
    time.sleep(2)

def searchForWordList(driver, wordList):
    for word in wordList:
        timeAndText('Searching for {}'.format(word))
        singleSearchBing(driver, word)
        # May needs a check if search was successfull
        timeAndText('Successfull searched for {}'.format(word))