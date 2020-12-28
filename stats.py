''' Collect all stats from Microsoft Rewards account '''
from selenium import webdriver
from textformat import timeAndText
import driver as d

def getCurrentLevel(driver: WebDriver):
    return driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/mee-rewards-user-status/div/mee-banner/div/div/div/div[1]/mee-banner-slot-1/mee-rewards-user-status-item/mee-rewards-user-status-profile/header/div/div/mee-persona/div[2]/persona-body/p[1]').text

def getAvailablePoints(driver: WebDriver):
    return driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/mee-rewards-user-status/div/mee-banner/div/div/div/div[2]/div[1]/mee-banner-slot-2/mee-rewards-user-status-item/mee-rewards-user-status-balance/div/div/div/div/div/p[1]/mee-rewards-counter-animation/span').text

def getAllTimePoints(driver: WebDriver):
    return driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/mee-rewards-user-status/div/mee-banner/div/div/div/div[2]/div[1]/mee-banner-slot-2/mee-rewards-user-status-item/mee-rewards-user-status-balance/div/div/div/div/div/p[3]/mee-rewards-counter-animation/span/b').text

def getPointsSpend(driver: WebDriver):
    return int(getAllTimePoints(driver)) - int(getAvailablePoints(driver))

def getCurrentStreak(driver: WebDriver):
    return driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/mee-rewards-user-status/div/mee-banner/div/div/div/div[2]/div[2]/mee-banner-slot-3/mee-rewards-user-status-item/mee-rewards-user-status-streak/div/div/div/div/div/p[1]/mee-rewards-counter-animation/span/b').text

def getAllStats(driver: WebDriver):
    pass