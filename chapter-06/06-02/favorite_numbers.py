########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           27/12/2022                     ###
########################################################

# This script will demonstrate dictionaries

favorite_numbers = {
    "john": 3,
    "sarah": 5,
    "michael": 1,
    "doug": 13,
    "sam": 7,
}

print(f'''John's favorite number is {favorite_numbers.get("john")}''')
print(f'''Sarah's favorite number is {favorite_numbers.get("sarah")}''')
print(f'''Michael's favorite number is {favorite_numbers.get("michael")}''')
print(f'''Doug's favorite number is {favorite_numbers.get("doug")}''')
print(f'''Sam's favorite number is {favorite_numbers.get("sam")}''')