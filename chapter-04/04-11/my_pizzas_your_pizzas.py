########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           24/12/2022                     ###
########################################################

# This script will demonstrate how copy a list

pizzas = ["pepperoni", "bacon", "chocolate"]

friend_pizzas = pizzas[:]

pizzas.append("ham")

friend_pizzas.append("mushroom")

print("My favourite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza}")

print("My friend'sfavourite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t{pizza}")    