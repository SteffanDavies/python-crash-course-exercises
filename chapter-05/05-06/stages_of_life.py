########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           27/12/2022                     ###
########################################################

# This script will demonstrate if-elif-else statements

age = 30

if age < 2:
    stage = "baby"
elif age >= 2 and age < 4:
    stage = "toddler"
elif age >= 4 and age < 13:
    stage = "kid"
elif age >= 13 and age < 20:
    stage = "teenager"
elif age >= 20 and age < 65:
    stage = "adult"
elif age >= 65:
    stage = "elder"

print(f"The person is: {stage}")