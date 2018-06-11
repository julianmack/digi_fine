"""SPEC: Please extract and derive the following information from the Wikipedia page about
Python (https://en.wikipedia.org/wiki/Python_(programming_language)) and output the following
items:
a) The name of “designed by” person for the Python programming language according to the
Wikipedia page.
b) Number of unique words in the ‘History’ session.
c) (Optional) Number of languages influenced by Python according to the Wikipedia page."""
import requests
import re
import json
from bs4 import BeautifulSoup
from lxml import html

#global
ADDRESS = "https://en.wikipedia.org/wiki/Python_(programming_language)"

ADDRESS1 = "https://en.wikipedia.org/wiki/Laurie_Cahill"


def main():
    r = requests.get(ADDRESS)

    data = r.text


    soup = BeautifulSoup(data, 'html.parser')

    tags = soup
    #a) find designed by:
    #This is in a table at top of the page
    num_tables = len(soup.find_all("table"))#

    #find which table it is in
    #^ideally using class_=**contains "infobox"
    #find th which contains "designed"
    #find sister element (which is a td)
    #save text



    #for tag in soup.find_all():
        #print(tag.name)

    #for title in soup.find_all('title'):
        #print (title.string)

    #print (soup.prettify())

        #print(soup.children)
    #print(soup.title)


"""
    headers = r.headers
    for key, value in headers.items():
        print (key, value)
    #data = json.loads(r.text)
    #data = r.json()

    jsonD = json.dumps(data)
    jsonL = json.loads(jsonD)
    print(type(jsonL))

"""


if __name__ == "__main__":
    main()
