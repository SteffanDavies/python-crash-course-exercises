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
    'set': 'An unordered series of unique items',
    'loop': 'A repeating structure of code based on a condition',
    'python': 'A high-level programming language',
    'vscode': 'An IDE with extensions for python development',
    'float': 'A data type representing a number with a floating decimal point',
}

for term, meaninng in glossary.items():
    print(f"{term}:")
    print(f"\t{meaninng}\n")