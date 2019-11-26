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



class SpiderFileTester(unittest.TestCase):

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





class IndeedForumFillTester(unittest.TestCase):

    applyBot = None

    def setUp(self):
         self.applyBot = ExpressApply()

    def applyWithNoLink(self):
        self.applyBot.addEmail('testEmail')
        self.applyBot.addName('jhon Smith')
        try:
            self.applyBot.applyTo()
        except Exception as e:
            self.fail()

    def addEmail(self):
        self.applyBot.addEmail('testEmail')

    def addName(self):
        self.applyBot.addName('testEmail')

    def applyCorrectly(self):
        self.applyBot.addEmail('testEmail')
        self.applyBot.addName('jhon Smith')
        L = 'https://www.indeed.com/viewjob?cmp=Havertys-Furniture-Companies&t=Retail+Sales+Consultant&jk=e5d59f3d51f031db&sjdu=QwrRXKrqZ3CNX5W-O9jEvZ793ZkrMSjbJmKrDbvG6ZioyIIOjzV35vrUfAIrEsV0Zu8NScqbgMmjtEe_wKP8jCzsP4fIgOrPqgPR449NdBo&adid=322682335&pub=4a1b367933fd867b19b072952f68dceb&vjs=3'
        try:
            self.applyBot.applyTo(L)
        except Exception as e:
            self.fail()
    def applyWithNoProfileTest(self):
        L = 'https://www.indeed.com/viewjob?cmp=Havertys-Furniture-Companies&t=Retail+Sales+Consultant&jk=e5d59f3d51f031db&sjdu=QwrRXKrqZ3CNX5W-O9jEvZ793ZkrMSjbJmKrDbvG6ZioyIIOjzV35vrUfAIrEsV0Zu8NScqbgMmjtEe_wKP8jCzsP4fIgOrPqgPR449NdBo&adid=322682335&pub=4a1b367933fd867b19b072952f68dceb&vjs=3'
        try:
            self.applyBot.applyTo(L)
        except Exception as e:
            self.fail()



if __name__ == '__main__':
    unittest.main()