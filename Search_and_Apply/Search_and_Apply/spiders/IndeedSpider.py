import scrapy

start_urls = ['https://www.indeed.com/']


class IndeedSpider(scrapy.Spider):
	name = 'Indeed'
	
	def parse(self, response):

		return scrapy.FormRequest.from_response(
			response,
			formid='text-input-what',
			formname = 'q',
			formdata={'what': 'CS'}
		)

		
def main():
	indeedSpider = IndeedSpider()
	response = scrapy.Request(url = start_urls[0])
	indeedSpider.parse(response)
	
main()