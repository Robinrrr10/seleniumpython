from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Google:
    def testSearch(self):
        localdriverPath = "/home/robin/drivers/chromedriver76/chromedriver";
        driver = webdriver.Chrome(localdriverPath)
        driver.get("https://www.google.com")
        sleep(4)
        title = driver.title
        print("Title is:", title)
        driver.find_element_by_name("q").send_keys("automation")
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        sleep(4)
        title = driver.title
        print("Title after search is:", title)
        driver.quit()
g1 = Google()
g1.testSearch()