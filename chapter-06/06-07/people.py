########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           27/12/2022                     ###
########################################################

# This script will demonstrate dictionaries

person_1 = {
    "first_name": "John",
    "last_name": "Doe",
    "age": "38",
    "city": "London",
}

person_2 = {
    "first_name": "Lizz",
    "last_name": "Frenz",
    "age": "23",
    "city": "Lisbon",
}

person_3 = {
    "first_name": "Marco",
    "last_name": "Correia",
    "age": "40",
    "city": "Madrid",
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person.get('first_name')} {person.get('last_name')}"
    age = person.get('age')
    city = person.get('city')
    info = f"{full_name} is {age} years old and from {city}"
    print(info)
