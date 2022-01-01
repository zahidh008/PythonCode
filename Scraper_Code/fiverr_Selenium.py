from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# import os

from time import sleep
# import scrapy

# from selenium.webdriver.remote.webelement import WebElement


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)

#driver=webdriver.Chrome()
driver.get("http://wad.ojooo.com/") 
# sleep(5)
# driver.get("https://fiverr.com")
#driver.manage().window().maximize()

#sleep(30)

#driver.get("https://www.fiverr.com/seller_dashboard")
# loginbtn = driver.find_elements_by_xpath("//li/a")

# for a in loginbtn:
#     if a.text=="Sign in":
#         a.click()
#         sleep(2)
#         break

# # driver.get("https://www.fiverr.com/login?source=top_nav")

# username = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='login']")))
# password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='password']")))
# button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

# # username = driver.find_element_by_id("login")
# # password = driver.find_element_by_id('password')

# # sleep(5)
# username.click()
# username.clear()
# username.send_keys("tahsinneha10@gmail.com")
# sleep(2)
# password.click()
# password.clear()
# password.send_keys("mam41643544@A")
# sleep(2)
# button.click()
# driver.find_element_by_class_name("MuiButton-label").click()
# time.sleep(2)
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







print("\n\n#################Sucess#####################")