import requests

response = requests.get("https://openlibrary.org/search/authors.json?q=t%20hobbes")


ids = ['OL50870A','OL4586796A','OL22242A']


for id in ids[:1]:
    response = requests.get("https://openlibrary.org/authors/{id}/works.json".format(id=id))
    print(response.json()['entries'][0])
