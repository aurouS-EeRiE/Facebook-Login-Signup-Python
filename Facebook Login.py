"""
Created on Mon Jun 29 22:11:08 2020

@author: aurouS_EeRiE
"""


from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get('https://facebook.com')
emailid= input('Enter your email id: ')
emailid1 = []
emailid1.append(emailid)
password = input("Enter your facebook id password: ")
for i in range(len(emailid1)):
    email_id = emailid1[i]
    emailbox = driver.find_elements_by_name('email')[0]
    emailbox.send_keys(email_id)
password1 = []
password1.append(password)
for i in range(len(password1)):
    paswd = password1[i]
    passwordbox = driver.find_elements_by_name('pass')[0]
    passwordbox.send_keys(paswd)
button = driver.find_elements_by_id('u_0_b')[0]
button.click()
sleep(120)