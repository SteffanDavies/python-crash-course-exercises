########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           27/12/2022                     ###
########################################################

# This script will demonstrate dictionaries

pet_1 = {
    "name": "Ollie",
    "type": "dog",
    "owner": "Sam"
}

pet_2 = {
    "name": "Rufus",
    "type": "dog",
    "owner": "Jayne"
}

pet_3 = {
    "name": "Smokey",
    "type": "cat",
    "owner": "Sheila"
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"""{pet.get("name")} is {pet.get("owner")}'s {pet.get("type")}.""")