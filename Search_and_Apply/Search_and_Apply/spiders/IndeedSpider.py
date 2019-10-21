import scrapy
from scrapy.crawler import CrawlerProcess

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
            Link = Links[i]))
      return data

class Job(scrapy.Item):
   Title = scrapy.Field()
   Link = scrapy.Field()


process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'items.json'
})

process.crawl(IndeedSpider)
process.start()





S = IndeedSpider()
print(IndeedSpider.start_requests())







































