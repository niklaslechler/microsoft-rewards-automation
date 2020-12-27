''' Actions on the microsoft page '''
import functions as f
from textformat import timeAndText
import time

# Check if login was successfull
def loginToMicrosoft(driver, email, password):
    timeAndText('Logging in to microsoft account')
    f.openPage(driver, 'https://login.live.com/login.srf')
    driver.find_element_by_name('loginfmt').send_keys(email)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input').click()
    time.sleep(3)
    driver.find_element_by_name('passwd').send_keys(password)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input').click()
    time.sleep(3)
    timeAndText('Login successfull')