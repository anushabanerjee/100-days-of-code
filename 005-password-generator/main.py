#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Easy - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# password=""
# for letter in range(0,nr_letters):
#   password+=random.choice(letters)
# for symbol in range(0,nr_symbols):
#   password+=random.choice(symbols)
# for number in range(0,nr_numbers):
#   password+=random.choice(numbers)

# print(password)

#Hard - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#!!!! Sorta works but bad logic and very generalised

# password=""
# passwordlength = nr_numbers + nr_letters + nr_symbols
# c1=  0
# c2 = 0 
# c3 = 0

#c1 is counter for letter
#c2 is counter for symbols
#c3 is counter for numbers

# for i in range(0,100):
#   ran = random.randint(1,3)
#   #if random number is 1, we print a letter, if 2 then symbol, if 3 then number
#   if ran == 1:
#     if c1 < nr_letters:
#       password+=random.choice(letters)
#       c1+=1
#   elif ran == 2:
#     if c2 < nr_symbols:
#       password+=random.choice(symbols)
#       c2+=1
#   elif ran == 3:
#     if c3 < nr_symbols:
#       password+=random.choice(numbers)
#       c3+=1


# print(password)

# List method (BEST)

password_list = []
password=""

for letter in range(0,nr_letters):
  password_list.append(random.choice(letters))
for symbol in range(0,nr_symbols):
  password_list.append(random.choice(symbols))
for number in range(0,nr_numbers):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

for char in password_list:
  password+=char
print("\nYour new password is: "+password)

#The following ones did not work.

#!!!! DID NOT WORK
# password = ""
# password_length = nr_letters + nr_numbers + nr_symbols
# randomlist = []
# for i in range(0,nr_letters):
#   randomlist.append("1")
# for i in range(0,nr_symbols):
#   randomlist.append("2")
# for i in range(0,nr_numbers):
#   randomlist.append("3")

# print(randomlist)
#!!!! DID NOT WORK

