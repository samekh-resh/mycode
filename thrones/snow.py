
import requests

choice = input("put in a random numer? ")
url = "https://www.anapioficeandfire.com/api/characters/"

apiUrl = url + choice

def main():

    #maing thehttp requests

    person = requests.get(apiUrl)
    person = person.json()

    print(person)

    houses = person["allegiances"]
    
    for x in houses:
       print(requests.get(x).json()["name"])
    
    #print(houses)

    books = person["books"]
    povBooks = person["povBooks"]
    books = books + povBooks
    
    for x in books:
        print(requests.get(x).json()["name"])



   # print(books)

main()
