# import webbrowser
# from time import sleep

# url = 'https://cgifederal.secure.force.com/scheduleappointment'

# while True:
#     print("refreshing...")
#     webbrowser.open(url, new=0, autoraise=False)
#     sleep(20)

from selenium import webdriver
import time

driver = webdriver.Edge()

driver.get('https://cgifederal.secure.force.com/scheduleappointment')
while True:
    time.sleep(20)
    driver.refresh()
# driver.quit()