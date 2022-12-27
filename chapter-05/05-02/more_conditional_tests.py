########################################################
###   Programmers:    Steffan Davies                 ###
###   Contact:        steffanclentdavies@gmail.com   ###
###   Date:           27/12/2022                     ###
########################################################

# This script will demonstrate conditionals

car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')


animal = 'dog'

print("Is animal == 'dog'? I predict True.")
print(animal == 'dog')

print("Is animal == 'cat'? I predict False.")
print(animal == 'cat')


food = 'pizza'

print("Is food == 'pizza'? I predict True.")
print(food == 'pizza')

print("Is food == 'salad'? I predict False.")
print(food == 'salad')


computer = 'linux'

print("Is computer == 'linux'? I predict True.")
print(computer == 'linux')

print("Is computer == 'mac'? I predict False.")
print(computer == 'mac')


phone = 'android'

print("Is phone == 'android'? I predict True.")
print(phone == 'android')

print("Is phone == 'ios'? I predict False.")
print(phone == 'ios')


# Inequality
browser = 'firefox'

print("Is browser != chrome? I predict True.")
print(browser != 'chrome')

print("Is browser != firefox? I predict False.")
print(browser != 'firefox')


# lower()

car = 'BMW'

print("Is car.lower() == bmw? I predict True.")
print(car.lower() == 'bmw')

print("Is car.lower() == nissan? I predict False.")
print(car.lower() == 'nissan')


# Numerical tests

age = 18

print("Is age == 18? I predict True.")
print(age == 18)
print("Is age != 18? I predict False.")
print(age != 18)
print("Is age > 17? I predict True.")
print(age > 17)
print("Is age < 17? I predict False.")
print(age < 17)
print("Is age >= 16? I predict True.")
print(age >= 16)
print("Is age <= 21? I predict True.")
print(age <= 21)

# and or

motorcycle = "kawasaki"

print("Is motorcycle kawasaki or honda? I predict True.")
print(motorcycle is "kawasaki" or motorcycle is "honda")

print("Is motorcycle kawasaki and honda? I predict False.")
print(motorcycle is "kawasaki" and motorcycle is "honda")


motorcycles = ["honda", "kawasaki", "suzuki", "yamaha"]
motorcycle = "keeway"

print("Is motorcycle in the japanese big 4? I predict False.")
print(motorcycle in motorcycles)

print("Is motorcycle not in the japanese big 4? I predict True.")
print(motorcycle not in motorcycles)



