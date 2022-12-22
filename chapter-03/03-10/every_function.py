########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           20/12/2022                     ###
########################################################

# This script will create a list and use every function learned until now

languages = ["English", "Portuguese", "German", "Japanese", "Arabic", "Cantonese", "Korean", "Spanish"]

# Print the complete list
print(languages)

# Print an element of the list
print(languages[1])

# Print the last element of the list
print(languages[-1])

# Changing an element of a list
languages[2] = "Dutch"

# Show the new list with a new element
print(languages)

# Append an element to the end of the list
languages.append("French")
print(languages)

# Insert an element in the list
languages.insert(4 ,"Hebrew")
print(languages)

# Remove an element of the list
del languages[1]
print(languages)

# Pop the last element of the list
popped_language = languages.pop()
print(popped_language)
print(languages)

# Pop the second element of the list
popped_language = languages.pop(1)
print(popped_language)
print(languages)

# Remove an element from the list by it's value
languages.remove("Hebrew")
print(languages)

# Sort the list without changing it's internal order
print(sorted(languages))

# Sort the list in reverse without changing it's internal order
print(sorted(languages, reverse=True))

# Sort the list and change it's internal order
languages.sort()
print(languages)

# Sort the list in reverse and change it's internal order
languages.sort(reverse=True)
print(languages)

# Reverse the list
languages.reverse()
print(languages)

# Find the length of the list
print(f"The list has {len(languages)} elements.")