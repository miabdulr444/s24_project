import click
import requests
from .utils import fetch_results4, sort_results_by_publication_year


@click.command(help='projectpack get_info')
@click.argument('keywords',nargs=-1, type=str)
def get_info(keywords):      
    # Endpoint for searching works with the provided keywords
    search_url = f'https://api.openalex.org/works?search={"".join(keywords)}'
    print("Search URL:", search_url)
    # Fetch all results for the current keyword
    all_results = fetch_results4(search_url)
    
    if all_results:
        # Sort the results by publication year from current year to latest year
        sorted_results = sort_results_by_publication_year(all_results)
        
        print(f"\nResults for keyword(s): '{''.join(keywords)}':\n")
        for idx, result in enumerate(sorted_results, 1):
            print(f"Result {idx}:")
            print("Title:", result.get('title', 'Title Not Available'))
            print("Publication Year:", result.get('publication_year', 'Publication Year Not Available'))
            
            authorships = result.get('authorships', [])
            authors = ','.join([author.get('author', {}).get('display_name', 'Unknown') for author in authorships])
            print("Authors:", authors)
            
            institutions = ','.join([','.join([inst.get('display_name', 'Unknown') for inst in author.get('institutions', [])]) for author in authorships])
            print("Institutions:", institutions)
            
            countries = ','.join(result.get('countries', ['Unknown']))
            print("Countries:", countries)
            
            cited_by_count = result.get('cited_by_count', 'Not Available')
            print("Cited By Count:", cited_by_count)
            
            print()
    else:
        print(f"No results found for keyword(s): '{''.join(keywords)}'.")


