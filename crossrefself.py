from __future__ import unicode_literals, print_function, absolute_import
import requests
from builtins import input
import difflib

from unidecode import unidecode

bare_url = "http://api.crossref.org/"



url = bare_url+"works"
requested = requests.get(url, "Big data and stream processing platforms for Industry 4.0 requirements mapping for a predictive maintenance use case")
print (requested.text)


def ask_which_is(title, items):
    found = False
    result = {}
    question = "\t It is >>'{}' article?\n y(yes)|n(no)|q(quit)"
    for item in items:
        w = input(question.format(
            unidecode(item["title"]), unidecode(title)))
        if w == "y":
            found = True
            result = item
            break
        if w == "q":
            break
    return found, result