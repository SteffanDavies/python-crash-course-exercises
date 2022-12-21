########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           20/12/2022                     ###
########################################################

# This script will demonstrate how to modify list elements

guests = ["Sharon", "James", "Phil"]

print(f"{guests[0]}, you are invited for dinner on New Year's Eve.")
print(f"{guests[1]}, you are invited for dinner on New Year's Eve.")
print(f"{guests[2]}, you are invited for dinner on New Year's Eve.")

print(f"{guests[1]} cannot make it for dinner...")

guests[1] = "Craig"

print(f"{guests[0]}, you are invited for dinner on New Year's Eve.")
print(f"{guests[1]}, you are invited for dinner on New Year's Eve.")
print(f"{guests[2]}, you are invited for dinner on New Year's Eve.")

print("We have found a larger table, so we should invite more guests.")

guests.insert(0, "Fred")
guests.insert(2, "Tina")
guests.append("Mike")

print(f"{guests[0]}, you are invited for dinner on New Year's Eve.")
print(f"{guests[1]}, you are invited for dinner on New Year's Eve.")
print(f"{guests[2]}, you are invited for dinner on New Year's Eve.")
print(f"{guests[3]}, you are invited for dinner on New Year's Eve.")
print(f"{guests[4]}, you are invited for dinner on New Year's Eve.")
print(f"{guests[5]}, you are invited for dinner on New Year's Eve.")

print("We can only have two people over afterall, the new table won't arrive in time.")

print(f"{guests.pop()}, I'm sorry but we have to do this another time.")
print(f"{guests.pop()}, I'm sorry but we have to do this another time.")
print(f"{guests.pop()}, I'm sorry but we have to do this another time.")
print(f"{guests.pop()}, I'm sorry but we have to do this another time.")

print(f"{guests[0]}, you are still invited.")
print(f"{guests[1]}, you are still invited.")

del guests[1]
del guests[0]

print(f"{guests}")