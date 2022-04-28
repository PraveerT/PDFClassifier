import requests

def doi2bib(doi):
  url = "http://dx.doi.org/" + doi

  headers = {"accept": "application/x-bibtex"}
  re = requests.get(url, headers = headers)
  return re.text


