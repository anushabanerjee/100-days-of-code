print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("You are at a road crossing. You can either take a left turn to the lake, or a right turn which goes downtown. Which way do you want to go? Left or Right?")
left_right = input ("Type L for Left and R for Right?\n")

if left_right == "L":
  print("You have reached the lake and notice that there is an island in the middle of it- one that you have never seen before.")
  yes_no = input("Do you want to go to the island? Y or N\n")
  if yes_no == "Y":
    print("There is an old wooden boat moored at the bank of the lake.Do you want to use the boat to reach the island, or swim across?")
    boat = input("Type boat or swim.\n")
    if boat == "boat":
      print("Nice! You used an old boat to go across to the island in the lake.\nOn reaching the island you notice that there is a table full of delicious fruits, bread, wine and cheese.")
      food = input("Do you taste something? Y or N\n")
      if food == "Y":
        fav_food = input("What is it that you decide to taste?\n")
        print(f"Yum!The {fav_food} was impeccable! A good decision.")
      red = input("Moving on, you see two doors- red and blue. Which one do you take?\n")
      if red == "red":
        print("Whoa! You open the red door, and ther is a small glowy little box on a table!")
        box = input("Do you want to open it? Y or N.\n")
        if box == "N":
          print("Come on! You have reached so far. Open it.")
        print("Opening the box, the light almost blinds you. When you get habituated, you find a screen which says \"Scan for Unlimited Amazon Vouchers\".\nCongratulations. You win unlimited Amazon vouchers!")
      else:
        print("You open the blue door and it takes you back to the lake.\nBut the island is gone.\nGame over.")
    else:
      print("Swimming in the lake is prohibited. The Lake Police grabs a hold of you. Game over.")
  else:
    print("You have no spirit of adventure. Game over.")
else:
  print("You recede into the boring city life. Game Over.")