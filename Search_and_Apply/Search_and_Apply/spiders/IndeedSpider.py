import scrapy
from scrapy.utils.response import open_in_browser
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.settings import Settings


class IndeedSpider(scrapy.Spider):
    name = "IndeedSpider"

    custom_settings ={
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': 'URLs_from_IndeedSpider.json',
        "TELNETCONSOLE_PORT" : None,
        'DOWNLOADER_MIDDLEWARES': None
        }

    start_urls = ["https://www.indeed.com/"]



    def __init__(self, searchItem='', *args, **kwargs):
      super(IndeedSpider, self).__init__(*args, **kwargs)
      self.search=searchItem


      print("##Indeed## " + searchItem)


    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            clickdata=None,
            formdata={'q': self.search },
            callback=self.getJob
        )

    def getJob(self, response):
      data = []
      jobs = response.xpath("//div[contains(@class,'jobsearch-SerpJobCard unifiedRow row result')]")
      for job in jobs:
          EZ = job.xpath("./table")
          if(EZ == []):
              continue
          title = job.xpath("./div/a/@title").get()
          link = job.xpath("./div/a/@href").get()
          company = job.xpath("./div/div/span/text()").get()

          data.append(Job(
              Title = title,
              Link = "https://www.indeed.com" +  link,
              Company = company.strip("\n")
          ))


      print("Indeed Done")


      return data
#      jobs1 = response.xpath("//div[contains(@class,'jobsearch-SerpJobCard unifiedRow row result')]").xpath("./div/a/@title").getall()
#      jobs2 = response.xpath("//div[contains(@class,'jobsearch-SerpJobCard unifiedRow row result')]").xpath("./div/a/@href").getall()
#      jobs3 = response.xpath("//div[contains(@class,'jobsearch-SerpJobCard unifiedRow row result')]").xpath("./div/div/span/text()").getall()
#      print(jobs1)
#      print(jobs2)
#      print(jobs3)
#      print('\n###############################\n')

# =============================================================================
#       print(len(jobs))
#       for job in jobs:
#            print(job)
#            title = job.xpath("./a").getall()
#            #link = job.xpath()
#            #print(link)
#            print(title)
#            print('\n###############################\n')
#            #print(job.xpath("./span[contains(@class, 'company')]").get()) #.xpath('./a/@title').getall()
# =============================================================================
                #Titles.append(job.xpath("./a/@title").get())
                #Links.append(job.xpath("./a/@href").get)








class Job(scrapy.Item):
   Title = scrapy.Field()
   Link = scrapy.Field()
   Company = scrapy.Field()


def searchFor(searchVar = '', start_urls = ["https://www.indeed.com/"], name = '', email = ''):
  settings = Settings()
  p = CrawlerRunner(settings)
  for thing in searchVar:
    p.crawl(IndeedSpider, searchItem=thing)
  p2 = p.join()
  p2.addBoth(lambda _: reactor.stop())

  if not reactor.running:
      reactor.run()
