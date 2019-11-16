import json

with open("URLs_from_IndeedSpider.json", 'r') as JSON:
    
    json_dict = json.load(JSON)
    
    type(json_dict)
    print(json_dict["Title"])