import requests
from bs4 import BeautifulSoup
import re


def letterboxd(desired_rating, username, normal_or_watchlist):
    page_number = 1
    movie_list = []

    while True:
        # 1 is normal mode, 2 is watchlist mode
        if normal_or_watchlist == '1':
            url = f'https://letterboxd.com/{username}/films/page/{page_number}/'
        elif normal_or_watchlist == '2':
            url = f'https://letterboxd.com/{username}/watchlist/page/{page_number}/'

        response = requests.get(url)

        # Make sure request worked
        if response.status_code == 200:
            # Scrape whole page (or what it allows at least)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the movie containers
            poster_containers = soup.find_all('li', class_='poster-container')

            if poster_containers:
                # Loop through each poster-container if any exist
                if normal_or_watchlist == '1':
                    for poster_container in poster_containers:
                        # Check if rating is high enough before adding
                        # Really shitty/redundant RE, come back and fix later
                        # Only do this if we aren't searching a watchlist, as a watchlist has no ratings
                        rating_span = poster_container.find('span', class_=re.compile(r'rated-(\d+)'))
                        # Check if the movie has a rating, go to next iteration if not
                        if rating_span:
                            rating_number = re.search(r'rated-(\d+)', ' '.join(rating_span.get('class'))).group(1)
                        else:
                            continue
                        if rating_number >= desired_rating:
                            # Had to access the img alt text as I think they close most stuff off from scraping, they left this in though
                            # Inefficient? find better method later
                            movie_list.append(poster_container.find('img')['alt'])
                    page_number += 1

                elif normal_or_watchlist == '2':
                    for poster_container in poster_containers:
                        # Same as before but without ratings
                        # There is probably a better way to do this, feels stupid to check watchlist var again after URL
                        movie_list.append(poster_container.find('img')['alt'])
                    page_number += 1

            else:
                break
        else:
            print('Could not connect to Letterboxd. Please make sure you spelled the username correctly.')
            return movie_list
    return movie_list

