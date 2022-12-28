########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           27/12/2022                     ###
########################################################

# This script will demonstrate dictionaries

favorite_places = {
    "Jane": ["Oslo", "Rome", "Paris"],
    "Mike": ["Chicago", "Atlanta"],
    "Lawrence": ["Ontario"],
}

for person, places in favorite_places.items():
    if len(places) > 1:
        print(f"{person}'s favorite places are:")
    elif len(places) == 1:
        print(f"{person}'s favorite place is:")
    for place in places:
        print(f"\t{place}")
    