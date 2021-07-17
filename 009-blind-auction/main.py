from replit import clear
from art import logo

#Printing the opening screen
print(logo)
print("Welcome to the Secret Auction.")

new_user={}
continue_bid = True
list_of_users=[]

#Function to find the highest bidder
def bid_winner(list_of_users):
    max_bid_index = 0

    #For loop to check which bid is the highest

    for position in range (len(list_of_users)):
       temp = list_of_users[position]["bid"]
       for pos in range (len(list_of_users)):
           temp2 = list_of_users[pos]["bid"]
           if temp2 > temp:
               max_bid_index = pos
    
    final_name = list_of_users[max_bid_index]["name"]
    final_bid = list_of_users[max_bid_index]["bid"]

    #Checking for Draws
    ctr = 0
    tie_bidder = []
    for pos in range (len(list_of_users)):
        temp_bid = list_of_users[pos]["bid"]
        if temp_bid == final_bid:
            tie_bidder.append(list_of_users[pos]["name"])
            ctr+=1
    
    if ctr == 1:
        print(f"The highest bid is ${final_bid}. Auction won by {final_name}")
    else:
        print("There is a tie between")
        for user in tie_bidder: 
            print (user, end = " ")

#Making a function to run for as long the user wants to input the secret bid
while continue_bid is True:
    #Taking user input
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: $"))

    new_user = {
        "name":name,
        "bid":bid 
    }

    list_of_users.append(new_user)

    left_to_bid= input("Is there anyone else left to bid? Y or N\n")
    if left_to_bid.lower() == "n":
        continue_bid = False
    elif left_to_bid.lower() == "y":
        clear()

bid_winner(list_of_users)