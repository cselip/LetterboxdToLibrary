from letterboxdscraper import *
from aadllibraryscraper import *
from msulibraryscraper import *

# Sets a base rating limit
username = input('What is the username of the profile you want to search? ')
normal_or_watchlist = input('Enter 1 to search movies already watched, enter 2 to search a watchlist.')
while normal_or_watchlist not in ['1', '2']:
    normal_or_watchlist = input('That was not a valid input! Please try again, 1 for movies watched, 2 for watchlist.')
if normal_or_watchlist == '1':
    desired_rating = input('What would you like the minimum rating out of 10 to be? ')
    while int(desired_rating) not in range(1, 11):
        desired_rating = input('That was not a valid input! Please try again, a number 1-10 please.')

else:
    # Setting to a random value if in watchlist mode, they won't need it anyway, movies aren't rated on watchlist
    desired_rating = 10
msuoraadl = input('Which library would you like to search? Enter 1 for AADL, 2 for MSU. ')
while msuoraadl not in ['1', '2']:
    msuoraadl = input('That was not a valid input! Please try again, 1 for AADL, 2 for MSU. ')

movies_to_search = letterboxd(desired_rating, username, normal_or_watchlist)
if msuoraadl == '1':
    for movie in aadllibrary(movies_to_search):
        print(movie)
elif msuoraadl == '2':
    for movie in msulibrary(movies_to_search):
        print(movie)
