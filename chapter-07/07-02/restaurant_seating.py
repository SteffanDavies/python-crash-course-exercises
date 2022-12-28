########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           28/12/2022                     ###
########################################################

# This script will demonstrate user input

message = input("How many people are in your dinner group? ")
message = int(message)

if message > 8:
    print("I'm sorry, you will have to wait a while.")
elif message > 0 and message <= 8:
    print("There is a table available.")