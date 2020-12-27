from datetime import datetime

def timeAndText(text):
    time = datetime.now().strftime('[%d/%m/%Y %H:%M:%S]')
    print('{} {}'.format(time, text))