########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           27/12/2022                     ###
########################################################

# This script will demonstrate if-elif-else statements

current_users = [
    "admin", 
    "craig892", 
    "Samantha_023", 
    "xXHiitXx", 
    "jackey_ch4n"
]

new_users = [
    "sssnoopy", 
    "daybreak55", 
    "samantha_023", 
    "dr3amlif3", 
    "jackey_ch4n"
]

current_users_lowercase = [name.lower() for name in current_users]

for user in new_users:
    if user.lower() in current_users_lowercase:
        print(f"Username {user} is already taken. Please choose another.")
    else:
        print(f"Username {user} is available.")