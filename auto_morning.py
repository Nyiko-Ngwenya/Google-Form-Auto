from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import password,username

class Automate:
    def __init__(self,username,password):
        self.driver = webdriver.Chrome('C:\webdrivers\chromedriver')
        self.driver.get("https://docs.google.com/forms/d/e/1FAIpQLScXfAF3epl6w9-3pz-RZWbeKkC9No4vlpDkahx5O6m6CLG70Q/viewform")
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").click()
        sleep(3)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
        sleep(3)
        self.morning()

    def morning(self):
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[1]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div').click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[3]/label/div').click()
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/textarea').send_keys('Upskilling')
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[2]/div[4]/div/div[2]/div[1]/div[2]/textarea').send_keys('No problems')
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div/div/div[3]/div[2]/div/div/span/span').click()
    
start = Automate(username,password)