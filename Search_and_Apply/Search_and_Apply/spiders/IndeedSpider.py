import scrapy
from scrapy.utils.response import open_in_browser
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from scrapy.http import HtmlResponse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class IndeedSpider(scrapy.Spider):
    name = "IndeedSpider"

    custom_settings ={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'URLs_from_IndeedSpider.json',
        "TELNETCONSOLE_PORT" : None
        }

    start_urls = ["https://www.indeed.com/"]

    def __init__(self, searchVar):
      self.search=searchVar


    def start_requests(self):
      yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            clickdata=None,
            formdata={'q': self.search},
            callback=self.getJob
        )

    def getJob(self, response):
      Titles = response.css('div.title').xpath("./a/@title").getall()
      Links = response.css('div.title').xpath("./a/@href").getall()
      data = []

      for i in range(len(Links)):
        data.append(Job(
            Title = Titles[i],
            Link = "https://www.indeed.com" +  Links[i]))

      return data


class Job(scrapy.Item):
   Title = scrapy.Field()
   Link = scrapy.Field()


class ApplySpider(scrapy.Spider):

    name = "ApplySpider"

    def __init__(self, linkVar, name, email):
      self.start_urls = linkVar
      self.username = name
      self.email = email
      self.options = webdriver.ChromeOptions()
      self.options.add_argument('headless')
      self.options.add_argument('window-size=1200x600')
      self.driver = webdriver.Chrome(chrome_options=self.options)


    def start_requests(self):
      yield scrapy.Request(url=self.start_urls[0], callback=self.parse)


    def parse(self, response):
      open_in_browser(response)
      print("\n"+ response.url+ "\n")


      self.driver.get(response.url)

      apply_button = self.driver.find_element_by_xpath('//*[@id="indeedApplyButtonContainer"]/span/div[2]/button/div')
      apply_button.click()
      WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "Apply Now")))
      self.driver.get_screenshot_as_file('debug.png')


      return scrapy.FormRequest.from_response(
            response,
            clickdata=None,
            formdata={'applicant.name': self.name,'applicant.email': self.email }
        )

def searchFor(searchVar):

    settings = Settings()
    process = CrawlerProcess(settings)
    settings.set('DOWNLOADER_MIDDLEWARES', None)
    for item in searchVar:
      process.crawl(IndeedSpider, item)
    process.start()

def applyTo(applyVar):
    settings = Settings()
    process = CrawlerProcess(settings)
    process.crawl(ApplySpider, applyVar[0], applyVar[1], applyVar[2])
    process.start()