import scrapy
from scrapy.utils.response import open_in_browser
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
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
      print("##Indeed##")


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
      print("Indeed Done")
      return data


class Job(scrapy.Item):
   Title = scrapy.Field()
   Link = scrapy.Field()


class ApplySpider(scrapy.Spider):

    name = "ApplySpider"

    def __init__(self, name='', email='', *args,**kwargs):
      super(ApplySpider, self).__init__(*args, **kwargs)
      self.username = name
      self.email = email
      options = webdriver.ChromeOptions()
      options.add_argument('headless')
      options.add_argument('window-size=1200x600')
      self.driver = webdriver.Chrome(chrome_options=options)
      print("##Apply##")



    def start_requests(self):
      yield scrapy.Request(url=self.start_urls, callback=self.parse)

    def parse(self, response):
      print("response.url")
      self.driver.get(response.url)

      print("Apply Done")
      return scrapy.FormRequest.from_response(
            response,
            clickdata=None,
            formdata={'applicant.name': self.name,'applicant.email': self.email }
        )



def searchFor(searchVar):
  settings = Settings()
  p = CrawlerRunner(settings)
  for item in searchVar:
    p.crawl(IndeedSpider, item=searchVar)
  p.addBoth(lambda _: reactor.stop())
  reactor.run()


def applyTo(applyVar):
  settings = Settings()
  p = CrawlerRunner(settings)
  p.crawl(ApplySpider, start_urls=applyVar[0], name=applyVar[1], email=applyVar[2])
  p.addBoth(lambda _: reactor.stop())
  reactor.run()
