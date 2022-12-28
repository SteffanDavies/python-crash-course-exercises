########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           28/12/2022                     ###
########################################################

# This script will demonstrate dictionaries

cities = {
    "tokyo": {
        "country": "japan",
        "population": 13.96,
        "fact": """The city was renamed Tokyo, meaning “eastern capital"."""
    },
    "lisbon":{
        "country": "portugal", 
        "population": 0.5, 
        "fact": """Archaeological evidence suggests the city has been inhabited since prehistoric ages."""
    },
    "london":{
        "country": "united kingdom", 
        "population": 8.98, 
        "fact": """London is the smallest city in England."""
    },
}

for city, description in cities.items():
    print(f"""{city.title()} is a city from {description.get("country").title()} with a population of {description.get("population")} million. {description.get("fact")}""")