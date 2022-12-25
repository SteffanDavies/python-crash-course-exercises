########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           25/12/2022                     ###
########################################################

# This script will demonstrate how copy and loop through lists

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(f"\t{food}")

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"\t{food}")