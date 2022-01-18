from itertools import count
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import os
import pickle
import time
import wget
import numpy
from numpy import savetxt
# import pandas
# import scrapy

# from selenium.webdriver.remote.webelement import WebElement


driver=webdriver.Chrome()

def fblogin():
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

def fblogin2():
    driver.get("https://www.facebook.com")
    time.sleep(2)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(2)
    driver.get("https://www.facebook.com")

def instalogin():
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name('password')

    username.clear()
    username.send_keys("Tanha632031")

    password.clear()
    password.send_keys("632031")

    time.sleep(2)
    button = driver.find_element_by_xpath("//button[@type='submit']")
    button.click()
    time.sleep(2)

def instalogin2():
    driver.get("https://www.instagram.com/")
    time.sleep(2)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    time.sleep(2)
    # driver.get("https://www.instagram.com/")
# login()
# login2()
# instalogin()
instalogin2()
print("Login completed")
time.sleep(2)
# accounturl = "https://www.instagram.com/efl_ana/"
accounturl = "https://www.instagram.com/therealpurnima/"
driver.get(accounturl)

def imgdownload():
    last_height = driver.execute_script("return document.body.scrollHeight")

    tryscrl = 0
    imgsinglink = []
    # for a in range(2):
    while True:
        imgs = driver.find_elements_by_class_name("_bz0w")
        for a in imgs:
            uniqlink = a.find_element_by_tag_name('a').get_attribute('href')
            if uniqlink not in imgsinglink:
                imgsinglink.append(uniqlink)
            # print(len(imgs))

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            tryscrl += 1
            print("Try = " + str(tryscrl))
        else:
            tryscrl = 0

        print("\n\n\n\nAll img links")
        print(len(imgsinglink))
        print(new_height)
        print(last_height)
        last_height = new_height

        if tryscrl >= 5:
            break

    print(imgsinglink)

    count = 0
    for a in imgsinglink:   
        driver.get(a)
        time.sleep(2)
        imglink = driver.find_element_by_class_name("_97aPb").find_element_by_tag_name('img').get_attribute('src')
        # print(imglink)

        path = "F:\Python\Instapic"
        # print(path)
        save_as = os.path.join(path, 'image_' + str(count) + '.jpg')
        wget.download(imglink, save_as)
        time.sleep(1)
        count += 1

path = "F:\Python\Instapic"

last_height = driver.execute_script("return document.body.scrollHeight")

tryscrl = 0

while True:
    

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        tryscrl += 1
        print("Try = " + str(tryscrl))
    else:
        tryscrl = 0

    last_height = new_height

    if tryscrl >= 5:
        break

imgs = driver.find_elements_by_class_name("_bz0w")
numbr = 0
for a in imgs:
    a.click()
    time.sleep(5)
    imglink = driver.find_element_by_class_name("_97aPb").find_element_by_tag_name('img').get_attribute('src')
    save_as = os.path.join(path, 'image_' + str(numbr) + '.jpg')
    wget.download(imglink, save_as)
    time.sleep(1)
    driver.find_element_by_class_name("NOTWr").click()
    time.sleep(5)
    numbr += 1

# a_file = open("F:\Python/test.txt", "w")
# for row in imgsinglink:
#     savetxt(a_file, row)

# a_file.close()

# savetxt(path + '/myfile.csv', imgsinglink, delimiter=',')
# imgsinglink.tofile(path + '/data2.csv', sep = ',')

# imgs = driver.find_elements_by_class_name("_bz0w")
# imgsinglink = []
# for a in imgs:
#     imgsinglink.append(a.find_element_by_tag_name('a').get_attribute('href'))











# for a in imglink:
#     print("Imglink = ")
#     print(a.get_attribute('innerHTML'))
#     print(a.get_attribute('src'))
# print(imglink.get_attribute('innerHTML'))
# imglink= imglink.get_attribute("src")


# path = os.getcwd()
# path = os.path.join(path, "InstaPic")
# os.mkdir(path)

# print("\nPath =")
# print(path)


# path = "F:\Python\Instapic"
# print(path)
# save_as = os.path.join(path, 'images.jpg')
# wget.download(imglink, save_as)

# counter = 0
# for image in images:
#     save_as = os.path.join(path, str(counter) + '.jpg')
#     wget.download(image, save_as)
# #     counter += 1

# grplink = "https://www.facebook.com/groups/286787079879268"
# grplink = "https://www.facebook.com/groups/easyenglishclub"



# loginbtn = driver.find_element_by_tag_name("button")
# print(loginbtn.get_attribute('innerHTML'))

# time.sleep(5)



# creatpostspans = driver.find_elements_by_xpath("//body//span")
# count = 0
# for a in creatpostspans:
#     count = count+1
#     txt = a.get_attribute('innerHTML')
#     if txt.find('Write something') != -1:
#         creatpostspan = a
#         break
# print(creatpostspan)
# creatpostspan.click()















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