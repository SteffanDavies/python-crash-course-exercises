########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           28/12/2022                     ###
########################################################

# This script will demonstrate user input

number = input("Please insert a number: ")
number = int(number)

remainder = number % 10

if remainder == 0:
    print("This number is a multiple of 10.")
else:
    print("This number is not a multiple of 10.")