from letterboxdscraper import *
from libraryscraper import *

# Sets a base rating limit
desired_rating = input('What would you like the minimum rating out of 10 to be?')
username = input('What is the username of the profile you want to search?')
# Use this instead of a normal for loop, don't want to revaluate container each time
print("\n".join(library(letterboxd(desired_rating, username))))
