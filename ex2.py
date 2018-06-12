"""SPEC:
Extract and derive the following information from the
Python Wikipedia page and output the following
items:
a) The name of “designed by” person for the Python
programming language according to the Wikipedia page.
b) Number of unique words in the ‘History’ session.
c) (Optional) Number of languages influenced by
Python according to the Wikipedia page."""

import sys
import requests
from bs4 import BeautifulSoup
import nltk
import string

#global
ADDRESS = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def main():
    #request webpage
    r = requests.get(ADDRESS)

    #HTML data
    data = r.text

    #create parse tree
    soup = BeautifulSoup(data, 'html.parser')

    #part_a
    [designer] = access_infobox(soup, "Designed")

    #part b
    history_txt = access_history(soup)
    unique_words = unique_tokens(history_txt)
    num_unique_words = len(unique_words)

    #part_c
    [influenced_by, influenced] = access_infobox(soup, "Influenced", True)
    #determine number of unique tokens
    num_influenced = len(unique_tokens([influenced]))

    #output results:
    print("\nRESULTS\n")
    print("Designed by:                    {}".format(designer))
    print("Number unique words in history: {}".format(num_unique_words))
    print("Number languages influenced:    {}\n".format(num_influenced))

def access_infobox(soup, phrase, next_row_req=False):
    """
    Returns detail from wiki infobox
    when given title keyphrase and bs4 object
    USAGE: access_infobox(bs4obj, keyphrase, flag)
    where flag is when title and description
    are on seperate rows

    Note: I used chrome developer mode to determine
    that required info was in a <table> with
    class= "infobox..." There is probably a more
    elegant way to work this out.
    """

    table = soup.find("table", class_="infobox")

    descriptions = []
    for row in table.find_all("tr"):
        if row.text:
            if phrase in row.text:
                if next_row_req == True:
                    row = row.find_next_sibling()
                description = row.td.text
                descriptions.append(description)

    #check at least one value returned:
    num_des = len(descriptions)
    if num_des is 0:
        print("Search terms not found. Try again")
        sys.exit(1)

    return descriptions

def unique_tokens(xs):
    """USAGE: pass list of strings,
    returns tokenized list of unique strings"""
    output = set()
    for x in xs:
        x = parse(x)
        tokens = nltk.word_tokenize(x)
        for token in tokens:
            output.add(token)
    return output

def parse(text):
    """Removes punctuation and digits"""
    text = text.translate(text.maketrans("", "", string.punctuation))
    text = text.translate(text.maketrans("", "", string.digits))
    return text

def access_history(soup):
    """Returns list of text from history section.
    History title stored with id="History"
    Wiki sections are not nested in a <div>.
    Therefore - must scroll through tags
    until reaching another heading
    where class="mw-headline"
    """
    elements = []
    for body_elem in soup.body.find_all(id="History"):
        elements.append(body_elem)

    #check length
    if len(elements) == 0:
        print("No elements returned. Widen search")
        sys.exit(1)
    elif len(elements) > 1:
        print("Too many elements returned. Refine search")
        sys.exit(1)

    #move up a level and skip "edit" <span>
    current_elem = elements[0].parent.find_next_sibling()

    #iterate through elements until next heading
    history_txt = []
    while current_elem.find(class_="mw-headline") == None:
        history_txt.append(current_elem.text)
        current_elem = current_elem.find_next_sibling()

    return history_txt


if __name__ == "__main__":
    main()
