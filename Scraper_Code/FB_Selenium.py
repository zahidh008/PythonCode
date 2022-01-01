from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# import os
import pickle
import time
# import scrapy

# from selenium.webdriver.remote.webelement import WebElement


driver=webdriver.Chrome()

def login():
    driver.get("https://www.facebook.com/login")
    #driver.manage().window().maximize()

    #username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='email']")))
    #password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='password']")))
    #button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))

    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id('pass')

    username.clear()
    username.send_keys("01733632031")

    password.clear()
    password.send_keys("632031")

    time.sleep(2)
    driver.find_element_by_name("login").click()
    time.sleep(2)

driver.get("https://www.facebook.com")
time.sleep(2)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(2)
driver.get("https://www.facebook.com")

#login()

grplink = "https://www.facebook.com/groups/286787079879268"
driver.get(grplink)
time.sleep(5)
creatpostspans = driver.find_elements_by_xpath("//body//span")
count = 0
for a in creatpostspans:
    count = count+1
    txt = a.get_attribute('innerHTML')
    if txt.find('Write something') != -1:
        creatpostspan = a
        break
print(creatpostspan)
creatpostspan.click()















pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
# url = "https://webapp.spypoint.com/camera/"
# driver.get(url)
# time.sleep(2)
# camera = driver.find_elements_by_class_name("jss25")
# url = url + camera[0].get_attribute('id')
# driver.get(url)
# time.sleep(5)
# imgs = driver.find_elements_by_tag_name("img")

# # camera[1].click()
# print("\n\n\nDataAll=")
# print(imgs)
# count = 0
# imgids=[10]
# for a in imgs:
#     if a.get_attribute('id'):
#         imgids[count] = a.get_attribute('id')
#         print("\nData"+str(count)+" =")
#         print(a.get_attribute('id'))
#         count +=1
# print(imgids)
# driver.get("https://webapp.spypoint.com/camera/603e895d6b07950015100242")
# time.sleep(2)
# driver.get("https://webapp.spypoint.com/camera/603e895d6b07950015100242/photo/61a3ccf866db6f0015cbb191")







print("\n\n\n\n#################Sucess#####################")