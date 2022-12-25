########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           25/12/2022                     ###
########################################################

# This script will demonstrate how to slice lists

numbers = list(range(1, 20, 2))

# First three odd numbers
print(f"The first three items in the list are: {numbers[:3]}")

# Middle of list odd numbers
print(f"The three items fromt he middle of the list are: {numbers[len(numbers)//2-1:len(numbers)//2+2]}")

# Last three odd numbers
print(f"The last three items in the list are: {numbers[-3:]}")

