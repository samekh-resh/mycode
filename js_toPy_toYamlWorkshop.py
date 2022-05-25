#!/usr/bin/python3


import json
import yaml

def main():

    with open("classdata.json", "r") as classData:
        classDataLoaded = json.load(classData)

    print(type(classDataLoaded))
    print(classDataLoaded)
    
    new = {
      "name":"gloopy",
      "awesome": False,
      "number": 21676,
      "favorites":{
          "movie":"The cure of Redemption",
          "ice cream":"salted pistachio",
          "color":"black"}
     }
    with open("cdEdited.yml", "w") as yamData:
        classDataLoaded.append(new)
        yaml.dump(classDataLoaded, yamData)





if __name__ == "__main__":
    main()
