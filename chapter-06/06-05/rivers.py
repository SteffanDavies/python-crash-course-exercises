########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           27/12/2022                     ###
########################################################

# This script will demonstrate looping through dictionaries

rivers = {
    'nile': 'egypt',
    'thames': 'united-kingdom',
    'tejo': 'portugal'
}

for river, country in rivers.items():
    print(f"The river {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())