''' General functions '''
from random_words import RandomWords
from textformat import timeAndText
import time

def getRandomWordList():
    list = []
    timeAndText('Generating random word list')
    while len(list) < 40:
        try:
            rw = RandomWords()
            list = rw.random_words(count=40)
        except:
            timeAndText('.')
            time.sleep(4)
    timeAndText('Random word list generated')