########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           27/12/2022                     ###
########################################################

# This script will demonstrate dictionaries

favorite_numbers = {
    "john": [3, 5, 4],
    "sarah": [5],
    "michael": [1, 6],
    "doug": [13, 7],
    "sam": [7],
}

for person, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"{person.title()}'s favorite numbers are:")
    elif len(numbers) == 1:
        print(f"{person.title()}'s favorite number is:")
    for number in numbers:
        print(f"\t{number}")