import requests
from bs4 import BeautifulSoup


def aadllibrary(movie_list):
    # The final list that main will print

    for i in movie_list:
        url = f'https://aadl.org/search/catalog/{i}?mat_code=u,g,q,zm'

        response = requests.get(url)

        # Make sure it worked
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the search result containers
            search_results = soup.find_all('div', class_='search-result l-overflow-clear')

            if search_results:
                # This is to make sure I don't check more than 3 results
                # I have never seen more than 3 versions of something, too rare of a case
                search_count = 0
                # Iterate through search results if they exist
                for search_result in search_results:
                    if search_count > 2:
                        break
                    # Get the title (formatted wrong for now) from search result class
                    result_to_analyze = search_result.find('a', class_='result-title').string
                    # Clean up format because they have weird newline and whitespace all over
                    result_ws_newline_removed = result_to_analyze.replace(' ', '').replace('\n', '')
                    # Compare result of both without WS and in lowercase
                    if result_ws_newline_removed.casefold() == i.replace(' ', '').casefold():
                        yield i
                        break
                    else:
                        search_count += 1
        else:
            print(f'Could not connect to AADL library for {i}')
    return
