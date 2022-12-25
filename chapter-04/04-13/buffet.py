########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           25/12/2022                     ###
########################################################

# This script will demonstrate how to create tuples

foods = ("hotdog", "pie", "lasagna", "beans", "pizza")

print("Our selection of foods:")
for food in foods:
    print(f"\t{food}")

# Error
#foods[0] = "hamburguer"

foods = ("paella", "pie", "lasagna", "beans", "steak")

print("Our new selection of foods:")
for food in foods:
    print(f"\t{food}")

