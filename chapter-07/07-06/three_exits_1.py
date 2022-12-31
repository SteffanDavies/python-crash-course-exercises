########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           31/12/2022                     ###
########################################################

# This script will demonstrate while loops and input

print("Welcome to the theater.")

asking = True

while asking:
    message = "What is your age? "
    age = int(input(message))

    if age >= 0 and age < 3:
        print("Your ticket is free.")
    elif age >= 3 and age < 12:
        print("Your ticket is 10$.")
    elif age >= 12:
        print("Your ticket is 15$.")
    # Use negative number to stop loop
    else:
        asking = False