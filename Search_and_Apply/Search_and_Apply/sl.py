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


wait = ui.WebDriverWait(driver, 5)
#wait.until(page_is_loaded)

driver.find_element_by_xpath('//*[@id="indeedApplyButtonContainer"]/span/div[2]/button/div').click()
#driver.find_elements(By.CLASS_NAME, "icl-Button icl-Button--branded icl-Button--md").click()

wait = ui.WebDriverWait(driver, 5)
#driver.quit()

# Identifying the "Python" tab by its XML id
#python_tab_id = 'ui-id-2'
#python_tab = driver.find_element_by_class_name(python_tab_id)
# "Clicking" on the tab
#python_tab.click()
