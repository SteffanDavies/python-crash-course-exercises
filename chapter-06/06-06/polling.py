########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           27/12/2022                     ###
########################################################

# This script will demonstrate looping through dictionaries

favorite_languages = {
    'jen': 'pyton',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'pyton',
}

people_to_poll = ["marcy", "edward", "daniel", "hassan"]

for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for taking the poll.")
    else:
        print(f"{person.title()}, we invite you to take the poll.")

