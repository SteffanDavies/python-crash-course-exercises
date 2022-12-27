########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           27/12/2022                     ###
########################################################

# This script will demonstrate dictionaries

glossary = {
    'variable': 'A "container" to store data',
    'string': 'A string of characters',
    'list': 'A mutable non-ordered sequence of data',
    'tuple': 'A non-mutable ordered sequence of data',
    'dictionary': 'A structure of key-value pairs',
}

print("variable:")
print(f"""\t{glossary.get("variable")}\n""")

print("string:")
print(f"""\t{glossary.get("string")}\n""")

print("list:")
print(f"""\t{glossary.get("list")}\n""")

print("tuple:")
print(f"""\t{glossary.get("tuple")}\n""")

print("dictionary:")
print(f"""\t{glossary.get("dictionary")}\n""")