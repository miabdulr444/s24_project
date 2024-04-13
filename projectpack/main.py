
from collections.abc import Iterable
import requests
import click
from operator import itemgetter

def fetch_results4(search_url):
    results = []
    while search_url:
        response = requests.get(search_url)
        if response.status_code == 200:
            data = response.json()
            results.extend(data.get('results', []))
            search_url = data.get('next')
        else:
            print("Error: Unable to retrieve search results.")
            break
    return results

def sort_results_by_publication_year(results):
    return sorted(results, key=lambda x: x.get('publication_year', float('inf')), reverse=True)

@click.command(help='OpenAlex get_info')
@click.argument('keyword', type=str)

def get_info(keyword):      
    keywords = keyword.split()
        #if multiple keywords are provided, use them as is
        #keywords = list(keywords)
    for keyword in keywords:
        # Endpoint for searching works with the provided keyword
        search_url = f'https://api.openalex.org/works?search={keyword}'
        print("Search URL:",search_url)
        # Fetch all results for the current keyword
        all_results = fetch_results4(search_url)
        
        if all_results:
            # Sort the results by publication year from current year to latest year
            sorted_results = sort_results_by_publication_year(all_results)
            
            print(f"\nResults for keyword: '{keyword}':\n")
            for idx, result in enumerate(sorted_results, 1):
                print(f"Result {idx}:")
                print("Title:", result.get('title', 'Title Not Available'))
                print("Publication Year:", result.get('publication_year', 'Publication Year Not Available'))
                
                authorships = result.get('authorships', [])
                authors = ', '.join([author.get('author', {}).get('display_name', 'Unknown') for author in authorships])
                print("Authors:", authors)
                
                institutions = ', '.join([', '.join([inst.get('display_name', 'Unknown') for inst in author.get('institutions', [])]) for author in authorships])
                print("Institutions:", institutions)
                
                countries = ', '.join(result.get('countries', ['Unknown']))
                print("Countries:", countries)
                
                cited_by_count = result.get('cited_by_count', 'Not Available')
                print("Cited By Count:", cited_by_count)
                
                print()
        else:
            print(f"No results found for keyword: '{keyword}'.")
