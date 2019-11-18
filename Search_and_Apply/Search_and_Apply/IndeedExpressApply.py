from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException




class ExpressApply():


    def __init__(self, name='', email=''):

      self.username = name
      self.email = email
      options = webdriver.ChromeOptions()
      options.add_argument('headless')
      options.add_argument('window-size=1200x600')
      self.driver = webdriver.Chrome(chrome_options=options)

      print("##Apply##")

    def applyTo(self, links):
        if isinstance(links, str):
            self.__apply__(links)
        elif all(isinstance(item, str) for item in links):
            for link in links:
                self.__apply__(link)
        else:
            raise TypeError


    def __apply__(self, link):


        driver = self. driver

        driver.get(link)

        apply_button = driver.find_element_by_xpath('//*[@id="indeedApplyButtonContainer"]/span/div[2]/button/div')
        apply_button.click()


        driver.switch_to_default_content()

        # Directing the driver to the popped up new frame

        wait = ui.WebDriverWait(driver, 20)
        frame = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/iframe")))
        driver.switch_to.frame(frame)
        wait.until(EC.frame_to_be_available_and_switch_to_it(0))

        # filling out the form

        # filling name
        text_name = driver.find_element_by_xpath("//*[@id='input-applicant.name']")
        try:
            wait = ui.WebDriverWait(driver, 20)
            text_name.clear()
            text_name.send_keys("John Smith")
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying to type title')
            text_name = driver.find_element_by_xpath("//*[@id='input-applicant.name']")
            text_name.clear()
            text_name.send_keys(self.name)

        # filling email
        text_email = driver.find_element_by_xpath('//*[@id="input-applicant.email"]')
        try:
            wait = ui.WebDriverWait(driver, 20)
            text_email.clear()
            text_email.send_keys("applysmith2345@gmail.com")
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying to type title')
            text_email = driver.find_element_by_xpath('//*[@id="input-applicant.email"]')
            text_email.clear()
            text_email.send_keys(self.email)

        # filling phone
        #text_phone = driver.find_element_by_xpath('//*[@id="input-applicant.phoneNumber"]')
        #try:
        #    wait = ui.WebDriverWait(driver, 20)
        #    text_phone.clear()
        #    text_phone.send_keys("111-222-3456")
        #except StaleElementReferenceException as Exception:
        #    print('StaleElementReferenceException while trying to type title')
        #    text_phone = driver.find_element_by_xpath('//*[@id="input-applicant.phoneNumber"]')
        #    text_phone.clear()
        #    text_phone.send_keys("111-222-3456")


        wait = ui.WebDriverWait(driver, 5)


