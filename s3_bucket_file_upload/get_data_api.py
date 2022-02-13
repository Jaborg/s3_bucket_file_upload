import requests
import csv


response = requests.get("https://openlibrary.org/search/authors.json?q=t%20hobbes")


ids = {'OL50870A':'Hobbes','OL4586796A':'Marquez','OL22242A':'Dostoyevsky'}


for id,author in ids.items():
    response = requests.get("https://openlibrary.org/authors/{id}/works.json".format(id=id))
    data = response.json()['entries']


    with open(f'{author}.csv', 'w', encoding='UTF-8') as f:

        writer = csv.DictWriter(f, fieldnames=['Works','Created'])
        # write the data
        writer.writeheader()

        for work in data:
            writer.writerow({'Works': work['title'],'Created': work['created']['value']})
