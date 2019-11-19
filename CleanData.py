#from Search_and_Apply.Search_and_Apply.spiders.IndeedSpider import searchFor, applyTo
import json

#convert list to dictionary



def CleanData():

  
  with open("URLs_from_IndeedSpider.json", 'r') as f:
    distros_dict = json.load(f)

  for distro in distros_dict:
    print(distro['Title'])

    
  print("\n")
  
  for distro in distros_dict:   
    print(distro["Link"])
    print("\n")
    


if __name__ == "__main__":
  
    CleanData()