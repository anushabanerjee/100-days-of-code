# Day 001
# Band Name Generator
# Program to take input from the user - name of a pet and home town - and turn it into a band name.

print("Hello!\nWelcome to Band Name Generator.")

# Taking input from user to enter the city name
city_name = input("Enter the name of the city you grew up in:\n")
print("Great! Nice place.")

fav_num = input("Enter your favourite number:\n")

# Ask the user for the name of a pet.
pet_name = input("Now enter the name of the first pet you had:\n")
print("Aww, that's cute!")

# Combine the name of their city and pet and show them their band name using string concatenation
print("Cool!\nHere is the name of your band: " + city_name + " " + pet_name + " " + fav_num)
