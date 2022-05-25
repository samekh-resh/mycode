#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""

import requests
import time;
import reverse_geocoder as rg
#print("IT WORKS")

url = "http://api.open-notify.org/iss-now.json"
listOfSites = []
def main():
    received = requests.get(url).json()
    lon = received['iss_position']['longitude']
    lat = received['iss_position']['latitude']
    dateAndTime = time.localtime(received['timestamp'])
    letTime = time.strftime("%a, %d %b %Y %H:%M", dateAndTime)
    #print(f"date and time: {letTime}")
    #print(f"CURRENT LOCATION OF ISS IS: \n lon:{lon}  \n lat:{lat}")
    coordsTuple = (lat, lon)
    name = rg.search(coordsTuple)[0]['name']
    county = rg.search(coordsTuple)[0]['cc']
    print(f"CURRENT LOCATION OF ISS IS: {letTime} \n lon:{lon}  \n lat:{lat} \n city: {name}, {county}")
    


if __name__ == "__main__":
    main()



