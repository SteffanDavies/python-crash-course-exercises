########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           20/12/2022                     ###
########################################################

# This script will demonstrate stripping strings of whitespace.

from email import message


famous_person = " Fidel Castro "

print(f"Original: \n\t{famous_person}")
print(f"Strip left: \n\t{famous_person.lstrip()}")
print(f"Strip right: \n\t{famous_person.rstrip()}")
print(f"Strip all: \n\t{famous_person.strip()}")