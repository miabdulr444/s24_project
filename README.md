# Projectpack

### Overview ###
Project Pack is a Python package that provides utility functions for various project tasks. It includes functions for greeting users, fetching search results from the OpenAlex works endpoint, and sorting search results by publication year.

### Installation ###
To install Project Pack, you can use pip:
pip install projectpack

### Usage ###
Hello Function
The hello function greets a person by name.

python
import projectpack
from projectpack import hello

greeting = hello("John")
print(greeting)  # Output: Hi there John

Fetch Results Function
The fetch_results function fetches search results from the OpenAlex api.

python
from projectpack.utils import fetch_results

results = fetch_results("https://api.openalex.org/works?search")
print(results)  # Output: List of search results

Sort Results Function
The sort_results_by_publication_year function sorts search results by publication year.

python
from projectpack.utils import sort_results_by_publication_year

sorted_results = sort_results_by_publication_year(results)
print(sorted_results)  # Output: Search results sorted by publication year

Project Pack

### Contributing ###
Contributions are welcome! Please feel free to submit bug reports, feature requests, or pull requests on GitHub.
