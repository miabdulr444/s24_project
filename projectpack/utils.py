import requests
from operator import itemgetter
from collections.abc import Iterable

def hello(name):
    return(f'Hi there {name}')

def fetch_results4(search_url):
    results = []
    while search_url:
        response = requests.get(search_url)
        if response.status_code == 200:
            data = response.json()
            results.extend(data.get('results',[]))
            search_url = data.get('next')
        else:
            return("Error: Unable to retrieve search results.")
            break
    return results

#def sort_results_by_publication_year(results):
    
def sort_results_by_publication_year(results):
    return sorted(results, key=lambda x: x.get('publication_year', float('inf')), reverse=True)





