import requests
from bs4 import BeautifulSoup
import re


def letterboxd(desired_rating, username):

    page_number = 1
    has_poster_container = True
    movie_list = []

    while has_poster_container:
        url = f'https://letterboxd.com/{username}/films/page/{page_number}/'

        # Send a GET request to the URL
        response = requests.get(url)

        # Make sure request worked
        if response.status_code == 200:
            # Scrape whole page (or what it allows at least)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the movie containers
            poster_containers = soup.find_all('li', class_='poster-container')

            if poster_containers:
                # Loop through each poster-container if any exist
                for poster_container in poster_containers:
                    # Check if rating is high enough before adding
                    # Really shitty/redundant RE, come back and fix later
                    rating_span = poster_container.find('span', class_=re.compile(r'rated-(\d+)'))
                    # Check if the movie has a rating, go to next iteration if not
                    if rating_span:
                        rating_number = re.search(r'rated-(\d+)', ' '.join(rating_span.get('class'))).group(1)
                    else:
                        page_number += 1
                        continue
                    if rating_number >= desired_rating:
                        # Had to access the img alt text as I think they close most stuff off from scraping, they left this in though
                        # Inefficient? find better method later
                        film_name = poster_container.find('img')['alt']
                        movie_list.append(film_name)
                page_number += 1
            else:
                has_poster_container = False
                break
        else:
            print("Couldn't connect to Letterboxd")
    return movie_list

