from selenium import webdriver
from time import sleep

class Google:
    def __init__(self,username,password):
        self.driver=webdriver.Chrome('C:\webdrivers\chromedriver')
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLScXfAF3epl6w9-3pz-RZWbeKkC9No4vlpDkahx5O6m6CLG70Q/viewform")

        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
        self.driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(3)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(2)
        self.driver.get('https://youtube.com')
        sleep(5)

# passw=open('New Text Document (2).txt',"r",encoding="utf-8")   
# password=str(passw.read())
# user=open('New Text Document (3).txt',"r",encoding="utf-8")   
# username=str(user.read())
mylike= Google('nyiko.ngwenya@umuzi.org','umuziacademy')