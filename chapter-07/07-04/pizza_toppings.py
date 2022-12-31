########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           31/12/2022                     ###
########################################################

# This script will demonstrate while loops and input

print("Please choose your list of toppings.")

topping = ""
while topping != "quit":
    message = "Which topping would you like: "
    topping = input(message)
    
    if topping != "quit":
        print(f"You have selected {topping}.")
