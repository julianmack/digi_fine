"""SPEC: Please extract and derive the following information from the Wikipedia page about
Python (https://en.wikipedia.org/wiki/Python_(programming_language)) and output the following
items:
a) The name of “designed by” person for the Python programming language according to the
Wikipedia page.
b) Number of unique words in the ‘History’ session.
c) (Optional) Number of languages influenced by Python according to the Wikipedia page."""
import sys
import requests
import re
import json
from bs4 import BeautifulSoup
from lxml import html
import nltk
import string

#global
ADDRESS = "https://en.wikipedia.org/wiki/Python_(programming_language)"

ADDRESS1 = "https://en.wikipedia.org/wiki/Laurie_Cahill"


def main():
    #request webpage
    r = requests.get(ADDRESS)

    #HTML data
    data = r.text

    #create parse tree
    soup = BeautifulSoup(data, 'html.parser')

    #part_a
    designer = part_a(soup)

    #part b - refactor common part a parts
    history_txt = []
    hist = []
    for body_elem in soup.body.find_all(id="History"):
        hist.append(body_elem)

    #check length
    if len(hist) == 1:
        pass
    else:
        print("refine search")
        sys.exit(1)

    #move up a level and skip "edit" <span>
    current_elem = hist[0].parent.find_next_sibling()

    #iterate through elements until next headline
    while current_elem.find(class_="mw-headline") == None:
        history_txt.append(current_elem.text)
        current_elem = current_elem.find_next_sibling()
        #print(current_elem)

    unique_words = tokenize(history_txt)
    num_words = len(unique_words)
    print (unique_words)


def tokenize(xs):
    output = set()
    for x in xs:
        x = parse(x)
        tokens = nltk.word_tokenize(x)
        for token in tokens:
            output.add(token)
    return output

def parse(text):
    text = text.translate(text.maketrans("", "", string.punctuation))
    text = text.translate(text.maketrans("", "", string.digits))
    return text

def part_a(soup):
    """
    a) find "designed by":
    This info is in a <table> at top of the page
    using developer mode (chrome) - in class "infobox vevent"
    """

    table = soup.find("table", class_="infobox")

    #find table headings
    designers = []
    for heading in table.find_all("th"):
        if heading.string:
            if "Designed" in heading.string:
                designer = heading.find_next_sibling().string
                designers.append(designer)

    #check there was only one value returned:
    num_des = len(designers)
    if num_des is 0:
        print("Search terms not found. Try again")
        sys.exit(1)
    elif num_des > 1:
        print("Multiple designers found. Refine search")
        sys.exit(1)

    return designer



"""
def find_all_tags():
    tags = set()
    for tag in soup.find_all():
        tags.add(tag.name
    return tags
"""
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
