import scrapy


class IndeedSpider(scrapy.Spider):
    name = "IndeedSpider"


    def start_requests(self):
        start_urls = ["https://www.indeed.com/"]
        yield scrapy.Request(url=start_urls[0], callback=self.parse)

    def parse(self, response):
      return scrapy.FormRequest.from_response(
            response,
            clickdata=None,
            formdata={'q': 'CS'},
            callback=self.getTitle
        )
    def getTitle(self, response):
      print(response.css('div.title').xpath("./a/@title").getall())