''' General functions '''

from random_word import RandomWords
from textformat import timeAndText
import time

def getRandomWordList():
    list = []
    while len(list) < 40:
        try:
            r = RandomWords()
            list = r.get_random_words()
            print(list)
        except:
            timeAndText('No word list generated... trying again.')
            time.sleep(2)
    timeAndText('Random word list geberated')