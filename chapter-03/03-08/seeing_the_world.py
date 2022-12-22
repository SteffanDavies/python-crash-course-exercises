########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           20/12/2022                     ###
########################################################

# This script will demonstrate sorting and reversing of lists with and without changing the original list

locations = ["Tokyo", "Moscow", "Beijing", "Sydney", "Dehli"]

print(locations)

print(sorted(locations))
print(locations)

print(sorted(locations, reverse=True))
print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)
