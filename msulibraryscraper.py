import requests
from bs4 import BeautifulSoup

# See library scraper for documentation, pretty much identical besides different tag search
def msulibrary(movie_list):
    movies_library_has = []
    for i in movie_list:
        url = f'https://catalog.lib.msu.edu/Search/Results?filter[]=~material-type_str_mv%3A%22Physical+Video+(DVD+or+Blu-ray)%22&filter[]=~material-type_str_mv%3A%22Streaming+Video%22&join=AND&bool0[]=AND&lookfor0[]={i}&type0[]=Title'

        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('a', class_='title getFull')
            if search_results:
                search_count = 0
                for search_result in search_results:
                    if search_count > 2:
                        break
                    result_to_analyze = search_result.string
                    result_ws_newline_removed = result_to_analyze.replace(' ', '').replace('\n', '')
                    if result_ws_newline_removed.casefold() == i.replace(' ', '').casefold():
                        movies_library_has.append(i)
                        break
                    else:
                        search_count += 1
        else:
            print(f'Could not connect to MSU library for {i}, continuing search for the rest')
    return movies_library_has