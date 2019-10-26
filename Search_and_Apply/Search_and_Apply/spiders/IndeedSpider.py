import scrapy
from scrapy.crawler import CrawlerProcess

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support import ui
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions as EC


class IndeedSpider(scrapy.Spider):
    name = "IndeedSpider"

    def start_requests(self):
        start_urls = ["https://www.indeed.com/"]
        yield scrapy.Request(url=start_urls[0], callback=self.parse)

    def parse(self, response):
      return scrapy.FormRequest.from_response(
            response,
            clickdata=None,
            formdata={'q': 'software engineer'},
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

    #def __init__(self):
        #self.driver = webdriver.Chrome()

    def start_requests(self):
      start_urls = ["https://www.indeed.com/rc/clk?jk=4f732a1edb258a0b&fccid=bdbc38ad07a162e4&vjs=3"]
      yield scrapy.Request(url=start_urls[0], callback=self.parse)

    def parse(self, response):
      return scrapy.FormRequest.from_response(
            response,
            clickdata=None,
            formdata={'applicant.name': 'John Smith','applicant.email': 'applysmith2345@gmail.com' },
            callback = self.open
        )
    def open(self, response):
      response.open_in_browser(response)


process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'jobs.json'
})

process.crawl(ApplySpider)