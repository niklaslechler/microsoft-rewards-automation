''' General functions '''
from random_words import RandomWords
from textformat import timeAndText
import time, json
import config as c
import stats as s
from datetime import datetime

''' Variables '''



''' Functions '''
def getRandomWordList():
    list = []
    timeAndText('Generating random word list')
    while len(list) < c.searchEntriesAmount:
        try:
            rw = RandomWords()
            list = rw.random_words(count=c.searchEntriesAmount)
        except:
            timeAndText('.')
            time.sleep(4)
    return list
    timeAndText('Random word list generated')

def timeAndText(text):
    time = datetime.now().strftime('[%d/%m/%Y %H:%M:%S]')
    print('{} {}'.format(time, text))

def closeScript(driver):
    writeLogoutData(driver)
    timeAndText('Closing script')
    driver.close()

def appendOnJson(filename: str, dict):
    with open(filename, 'w') as f:
        f.write(json.dumps(dict))

def readFromJson(filename: str, key):
    with open(filename, 'r') as f:
        pass
        #return f.read

def logInOutData(driver, action: str):
    timeAndText('Saving {} data'.format(action))
    return { 
    "action" : action,
	"date" : datetime.now().strftime('%d/%m/%Y'),
    "time" : datetime.now().strftime('%H:%M:%S'),
    "level" : s.getCurrentLevel(driver),
    "streak" : s.getCurrentStreak(driver),
    "points-overall" : s.getAllTimePoints(driver),
    "points-spend" : s.getPointsSpend(driver),
    "points-available" : s.getAvailablePoints(driver)
    }

def writeLoginData(driver):
    appendOnJson('log.json', logInOutData(driver, 'login'))

def writeLogoutData(driver):
    appendOnJson('log.json', logInOutData(driver, 'logout'))