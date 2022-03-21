from selenium import webdriver
import time
browser = webdriver.Chrome("/home/desktop/chromedriver")
browser.get("https://www.instagram.com/")
time.sleep(3)
username=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
username.send_keys("your Username")
time.sleep(3)
password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("your password")
password.submit()
time.sleep(3)

notnow=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
notnow.click()
time.sleep(3)

Noti=browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
Noti.click()
time.sleep(3)

def firstpic():
    time.sleep(3)
    pic=browser.find_element_by_class_name("_9AhH0")
    pic.click()
def comment():
    time.sleep(3)
    comment=browser.find_element_by_class_name("PUqUI Ypffh")
    commentarea.click()
    time.sleep(3)
    commentarea=browser.find_element_by_class_name("PUqUI Ypffh")
    commentarea.click()
    commentarea.send_keys("This is test comment")
    commentarea.submit()
