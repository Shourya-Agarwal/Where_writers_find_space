from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Hottest(LiveServerTestCase):
    def img_scrapper(self,keywords):
            options = webdriver.ChromeOptions()
            options.headless = True
            driver = webdriver.Chrome('C:\\Users\\Agarw\\OneDrive\\Desktop\\fyppp\chromedriver.exe',options=options)
            driver.get('https://www.google.com/')
            
            box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            data=''
            for i in keywords:
                data+=i+" "
            box.send_keys(data)
            box.send_keys(Keys.ENTER)
            
            driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
            
            
            #Will keep scrolling down the webpage until it cannot scroll no more
            last_height = driver.execute_script('return document.body.scrollHeight')
            while True:
                driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(2)
                new_height = driver.execute_script('return document.body.scrollHeight')
                try:
                    driver.find_element_by_xpath('//*[@id="islrg"]/div/div/div/div/div[5]/input').click()
                    time.sleep(2)
                except:
                    pass
                if new_height == last_height:
                    break
                last_height = new_height
            
            # getting all image links and storing in the lis
            lis=[]
            for i in range(1, 100):
                try:
                    link=driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img')
                    img=link.get_attribute("src")
                    lis.append(img)
                except:
                    pass
            
            return lis
        
