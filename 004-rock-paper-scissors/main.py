import random

print("Let's play!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = input("Rock, Paper or Scissors? ")

if user.lower () == "rock" or user.lower() == "paper" or user.lower() == "scissors" or user.lower() == "scissor":
  row1 = ["T","W","L"]
  row2 = ["L","T","W"]
  row3 = ["W","L","T"]

  win_lose_grid = [row1,row2,row3]
  print("You chose:")
  
  if user.lower() == "rock": 
    user_choice = 0
    print (rock)
  elif user.lower() == "paper":
    user_choice = 1
    print (paper)
  elif user.lower() == "scissors" or user.lower() == "scissor":
    user_choice = 2
    print (scissors)
  comp_choice = random.randint(0,2)
  print("Computer chose:")
  if comp_choice == 0:
    print(rock)
  elif comp_choice == 1:
    print(paper)
  elif comp_choice == 2:
    print(scissors)

  winner = win_lose_grid[comp_choice][user_choice]

  if winner == "W":
    print("Congratulations! You win!")
  elif winner == "L":
    print("Too bad. You lose.")
  elif winner == "T":
    print("It's a Tie!")
else:
  print(f"{user} is not an acceptable response. Press RUN to play again.")




