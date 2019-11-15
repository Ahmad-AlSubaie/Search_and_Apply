import scrapy
from scrapy.utils.response import open_in_browser
from twisted.internet import reactor
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
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': 'URLs_from_IndeedSpider.json',
        "TELNETCONSOLE_PORT" : None,
        'DOWNLOADER_MIDDLEWARES': None
        }

    start_urls = ["https://www.indeed.com/"]

    def __init__(self, item='', *args, **kwargs):
      super(IndeedSpider, self).__init__(*args, **kwargs)
      self.search=item


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

    def __init__(self, name='', email='', *args,**kwargs):

      self.username = name
      self.email = email
      options = webdriver.ChromeOptions()
      options.add_argument('headless')
      options.add_argument('window-size=1200x600')
      self.driver = webdriver.Chrome(chrome_options=options)
      super(ApplySpider, self).__init__(*args, **kwargs)



    def start_requests(self):
      yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):

      print("#################\n")
      self.driver.get(response.url)



      apply_button = self.driver.find_element_by_xpath('//*[@id="indeedApplyButtonContainer"]')
      apply_button.click()

      self.driver.implicitly_wait(5)


      #frame = self.driver.find_element_by_xpath('//*[@id="indeedapply-modal-preload-iframe"]/html/body/iframe')
      #self.driver.switch_to.frame(frame)
      #frame = self.driver.find_element_by_xpath("")
      #self.driver.switch_to.frame(frame)

      #self.driver.get_screenshot_as_file('/debug.png')


      #body = self.driver.page_source
      #response = HtmlResponse(self.driver.current_url, body=body, encoding='utf-8')

      return scrapy.FormRequest.from_response(
            response,
            clickdata=None,
            formdata={'applicant.name': self.name,'applicant.email': self.email }
        )


def searchFor(searchVar):
  if reactor.running:
      reactor.stop()
  settings = Settings()
  p = CrawlerProcess(settings)
  __searchFor(searchVar, p)
  reactor.run()


def applyTo(applyVar):
  if reactor.running:
      reactor.stop()
  settings = Settings()
  p = CrawlerProcess(settings)
  __applyTo(applyVar, p)
  reactor.run()


def __searchFor(searchVar, p):
    for item in searchVar:
      p.crawl(IndeedSpider, item=searchVar)


def __applyTo(applyVar, p):
    p.crawl(ApplySpider, start_urls=applyVar[0], name=applyVar[1], email=applyVar[2])
