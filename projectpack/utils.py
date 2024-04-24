"""Module containing functions for projectpack."""

import requests
from operator import itemgetter
from collections.abc import Iterable


def hello(name):
    """

    Greet a person by name.

    Args
    ----
        name (str): The name of the person.


    Returns
    -------
        str: A greeting message.

    """
    return f"Hi there {name}"


def fetch_results4(search_url):
    """

    Fetch results from a search URL.

    Args
    ----
        search_url (str): The URL to fetch search results from.


    Returns
    -------
        list: A list of search results.
    """
    results = []
    try:
        while search_url:
            response = requests.get(search_url)
            if response.status_code == 200:
                data = response.json()
                results.extend(data.get("results", []))
                search_url = data.get("next")
            else:
                return "Error: Unable to retrieve search results."
    except Exception as e:
        print(f"An error occurred: {e}")

    return results


def sort_results_by_publication_year(results):
    """

    Sort search results by publication year.

    Args
    ----
        results (list): A list of search results.


    Returns
    -------
        list: A list of results sorted by publication year.

    """
    try:
        return sorted(
            results, key=lambda x: x.get("publication_year", float("inf")), reverse=True
        )
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
