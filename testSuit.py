import unittest
import jsonlines

from Search_and_Apply.Search_and_Apply.spiders.IndeedSpider import searchFor
from Search_and_Apply.Search_and_Apply.IndeedExpressApply import ExpressApply

class TestFileContent(unittest.TestCase):

    def setUpClass(self):
        searchFor('art')


    #def tearDownClass(self):
        #clean up

    def fileWriteReadTest(self):
        with open("URLs_from_IndeedSpider.json", mode ='w') as f:
            f.write('')
        f.close()

        data = 'STUFF'
        with open("URLs_from_IndeedSpider.json", mode ='r') as f:
            data = f.read()
        f.close()

        self.assertTrue(data, '')
        self.assertFalse(data, 'stuff')



class SpiderFileTester  (unittest.TestCase):

    def SpiderHasLinks(self):
        with jsonlines.open("URLs_from_IndeedSpider.json", mode ='r') as reader:
            distros_dict = reader.iter(type = dict)
            for link in distros_dict:
                self.assertFalse(link['Link'], '')  #make sure that no links are empty
                self.assertIn('https://www.indeed.com/', link['Link'])

    def SpiderSearch(self):
        try:
            searchFor(['art', 'math'])
            searchFor(['art', 'math'])
        except Exception as e2:
            self.fail()




if __name__ == '__main__':
    unittest.main()