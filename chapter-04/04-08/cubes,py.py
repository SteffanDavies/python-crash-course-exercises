########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           24/12/2022                     ###
########################################################

# This script will demonstrate how use step to print cubes of numbers in range

cubes = []

for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
    print(cube)