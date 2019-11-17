from Search_and_Apply.Search_and_Apply.spiders.IndeedSpider import searchFor, applyTo
import json


def main():

  #get user input for search terms
  #save search tems to list_to_search


  list_to_search = ['software engineer', 'art']
  searchFor(list_to_search) #and writes the resultes to URLs_from_IndeedSpider

  #open file URLs_from_IndeedSpider
  #save relavent links to list_of_links

  list_of_links = ['https://www.indeed.com/viewjob?cmp=Catalyte&t=Become+Software+Developer+No+Experience&jk=1bcef3d9fc1b0b32&sjdu=QwrRXKrqZ3CNX5W-O9jEvW16Yhk4ozNCdaWKrMunypsF4bpKjscnMnzPFjGwUT8pmTq0NikKnfo91oL8LEaz9PmFE3FVkgBqhjy5aD2O7I6Oveef6XgOIAsWlCpqPX_L&adid=321198033&pub=4a1b367933fd867b19b072952f68dceb&vjs=3']

  applyTo([list_of_links , 'John Smith', 'applysmith2345@gmail.com'])


main()