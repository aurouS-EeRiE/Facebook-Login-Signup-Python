"""
Created on Mon Jun 29 22:12:50 2020

@author: aurouS_EeRiE
"""


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.get('https://facebook.com')

firstname = input('Enter your first name : ')
firstname1 = []
firstname1.append(firstname)
for i in range(len(firstname1)):
    first_name = firstname1[i]
    name_1 = driver.find_elements_by_name('firstname')[0]
    name_1.send_keys(first_name)

lastname = input('Enter your last name : ')
lastname1 = []
lastname1.append(lastname)
for i in range(len(lastname1)):
    last_name = lastname1[i]
    name_2 = driver.find_elements_by_name('lastname')[0]
    name_2.send_keys(last_name)

emailid= input('Enter your email id or mobile number: ')
emailid1 = []
emailid1.append(emailid)
for i in range(len(emailid1)):
    email_id = emailid1[i]
    emailbox = driver.find_elements_by_name('reg_email__')[0]
    emailbox.send_keys(email_id)


password = input("Enter your facebook id password: ")
password1 = []
password1.append(password)
for i in range(len(password1)):
    paswd = password1[i]
    passwordbox = driver.find_elements_by_name('reg_passwd__')[0]
    passwordbox.send_keys(paswd)


DOB_D = input('Enter your date : ')
element_1= Select(driver.find_element_by_id('day'))
element_1.select_by_value(DOB_D)
DOB_M = input('Enter your Month : ')
element_2= Select(driver.find_element_by_id('month'))
element_2.select_by_value(DOB_M)
DOB_Y = input('Enter your Year : ')
element_3= Select(driver.find_element_by_id('year'))
element_3.select_by_value(DOB_Y)

gender = int(input("1. Female \n2.Male \n3.Custom \nEnter 1 or 2 or 3: "))
if (gender == 1):
    gen = driver.find_element_by_id("u_0_6")
    gen.click()
elif (gender == 2):
    gen = driver.find_element_by_id("u_0_7")
    gen.click()
elif (gender == 3):
    gen = driver.find_element_by_id("u_0_8")
    gen.click()
    pick = Select(driver.find_element_by_name('preferred_pronoun'))
    pronoun = int(input('Select a Pronoun: \n1. She: "Wish her a happy birthday!" \n2.He: "Wish him a happy birthday!" \n3. They: "Wish them a happy birthday!" \nEnter 1 or 2 or 3: '))
    if (pronoun == 1):
        pick.select_by_value('1')
    elif (pronoun == 2):
        pick.select_by_value('2')
    elif (pronoun == 3):
        pick.select_by_value('6')
signup = driver.find_element_by_name('websubmit')
signup.click()
print("\nSuccessfull!!!")