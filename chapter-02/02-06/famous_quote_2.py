########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           20/12/2022                     ###
########################################################

# This script will demonstrate sanitizing strings and using format print to display a quote from a famous historical figure.

from email import message


famous_person = " fidel Castro "
message = "Men do not shape destiny. Destiny produces the man for the hour."

print(f'{famous_person.strip().title()} once said, "{message}"')