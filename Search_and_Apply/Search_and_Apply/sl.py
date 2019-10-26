# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 09:33:32 2019

@author: bkermani
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
 
# The place we will direct our WebDriver to
url = 'https://www.indeed.com/viewjob?cmp=Aerial-Applications&t=Software+Engineer&jk=43762dd1181cf6e5&sjdu=QwrRXKrqZ3CNX5W-O9jEvRFd8FQI4DEv5V74lSpSnHbLKoAgTb-l0dtsJtwgxNtDoV2VvnXtXXu0Jl2SyiV3zA&tk=1dnkn8q6ep89c800&adid=293177593&pub=4a1b367933fd867b19b072952f68dceb&vjs=3'
# Creating the WebDriver object using the ChromeDriver
driver = webdriver.Chrome()
# Directing the driver to the defined url
driver.get(url)

#wait = ui.WebDriverWait(driver, 5)

# storing the current window handle to get back to dashbord 
main_page = driver.current_window_handle
#apply_page = None

apply_button = driver.find_element_by_xpath('//*[@id="indeedApplyButtonContainer"]/span/div[2]/button/div')
apply_button.click()

#wait = ui.WebDriverWait(driver, 5)


#/html/body/iframe 
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/iframe")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-applicant.name"]'))).send_keys("John Smith")
# change the control to apply page        
#driver.switch_to.window(apply_page) 
#driver.switch_to.frame(driver.find_element_by_xpath("/html/body/iframe"))

# changing the handles to access login page 
"""while not apply_page:
    for handle in driver.window_handles:
        if handle != main_page:
            apply_page = handle 
            break
            """ 
            
# Now we are in the popup window
#text_name = driver.find_element_by_xpath("//*[@id='input-applicant.name']")
#text_name.clear()
#text_name.send_keys("John Smith")
#wait = ui.WebDriverWait(driver, 5)

"""text_email = driver.find_element_by_xpath('//*[@id="input-applicant.email"]')
text_email.clear()
text_email.send_keys("sohnsmith@email.com")"""

"""text_phone = driver.find_element_by_xpath('//*[@id="input-applicant.phoneNumber"]')
text_phone.clear()
text_phone.send_keys("222-333-4444")"""

#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)

wait = ui.WebDriverWait(driver, 5)

# switch back to parent window

###################
#driver.quit()


