########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           28/12/2022                     ###
########################################################

# This script will demonstrate dictionaries

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'profession' : 'physicist',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'profession': 'physicist',
    },
    'ntesla': {
        'first': 'nikola',
        'last': 'tesla',
        'location': 'styria',
        'profession': 'engineer',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info.get('first')} {user_info.get('last')}"
    location = f"{user_info.get('location')}"
    profession = f"{user_info.get('profession')}"

    print(f"\t{full_name.title()}")
    print(f"\t{location.title()}")
    print(f"\t{profession.title()}")