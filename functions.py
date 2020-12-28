''' General functions '''
from random_words import RandomWords
from textformat import timeAndText
import time
import config as c

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