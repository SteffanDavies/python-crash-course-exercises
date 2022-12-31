########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           31/12/2022                     ###
########################################################

# This script will demonstrate while loops and input

print("Welcome to the theater.")

while True:
    message = "What is your age? "
    user_input = input(message)

    if user_input == "quit":
        break

    age = int(user_input)

    if age >= 0 and age < 3:
        print("Your ticket is free.")
    elif age >= 3 and age < 12:
        print("Your ticket is 10$.")
    elif age >= 12:
        print("Your ticket is 15$.")
    else:
        print("Invalid age.")
    
    
    