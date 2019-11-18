from Search_and_Apply.Search_and_Apply.spiders.IndeedSpider import searchFor
from Search_and_Apply.Search_and_Apply.IndeedExpressApply import ExpressApply
import json


def main():

  #get user input for search terms
  #save search tems to list_to_search

  list_of_links = ['https://www.indeed.com/viewjob?cmp=Catalyte&t=Become+Software+Developer+No+Experience&jk=1bcef3d9fc1b0b32&sjdu=QwrRXKrqZ3CNX5W-O9jEvW16Yhk4ozNCdaWKrMunypsF4bpKjscnMnzPFjGwUT8pmTq0NikKnfo91oL8LEaz9PmFE3FVkgBqhjy5aD2O7I6Oveef6XgOIAsWlCpqPX_L&adid=321198033&pub=4a1b367933fd867b19b072952f68dceb&vjs=3']


<<<<<<< Updated upstream
  list_to_search = ['software engineer', 'art']
  searchFor(list_to_search, list_of_links) #and writes the resultes to URLs_from_IndeedSpider
=======
  applyBot = ExpressApply('John Smith', 'applysmith2345@gmail.com')
>>>>>>> Stashed changes

  list_to_search = ['art']

  searchFor(list_to_search)

<<<<<<< Updated upstream
  applyTo([list_of_links , 'John Smith', 'applysmith2345@gmail.com'])



=======
  list_of_links = ['https://www.indeed.com/viewjob?cmp=Catalyte&t=Become+Software+Developer+No+Experience&jk=1bcef3d9fc1b0b32&sjdu=QwrRXKrqZ3CNX5W-O9jEvW16Yhk4ozNCdaWKrMunypsF4bpKjscnMnzPFjGwUT8pmTq0NikKnfo91oL8LEaz9PmFE3FVkgBqhjy5aD2O7I6Oveef6XgOIAsWlCpqPX_L&adid=321198033&pub=4a1b367933fd867b19b072952f68dceb&vjs=3']

  applyBot.applyTo([list_of_links ])


  input("press any button to close...\n")
>>>>>>> Stashed changes
main()