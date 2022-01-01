from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# import os

import time
# import scrapy

# from selenium.webdriver.remote.webelement import WebElement


driver=webdriver.Chrome()
  
driver.get("https://webapp.spypoint.com/login")
#driver.manage().window().maximize()

#username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='email']")))
#password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='password']")))
#button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit']")))

username = driver.find_element_by_id("email")
password = driver.find_element_by_id('password')


username.clear()
username.send_keys("rcollazo@gmail.com")
#username.click()
password.clear()
password.send_keys("Hg7Zvbgss*&")
#password.click()
time.sleep(2)
driver.find_element_by_class_name("MuiButton-label").click()
time.sleep(2)
url = "https://webapp.spypoint.com/camera/"
driver.get(url)
time.sleep(2)
camera = driver.find_elements_by_class_name("jss25")
url = url + camera[0].get_attribute('id')
driver.get(url)
time.sleep(5)
imgs = driver.find_elements_by_tag_name("img")

# camera[1].click()
print("\n\n\nDataAll=")
print(imgs)
count = 0
imgids=[10]
for a in imgs:
    if a.get_attribute('id'):
        imgids[count] = a.get_attribute('id')
        print("\nData"+str(count)+" =")
        print(a.get_attribute('id'))
        count +=1
print(imgids)
# driver.get("https://webapp.spypoint.com/camera/603e895d6b07950015100242")
# time.sleep(2)
# driver.get("https://webapp.spypoint.com/camera/603e895d6b07950015100242/photo/61a3ccf866db6f0015cbb191")







print("\n\n\n\n#################Sucess#####################")