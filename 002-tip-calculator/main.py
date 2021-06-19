# Day 002
# Tip calculator
# Program to calculate tips from the bill number, percentage, and number of people paying the bill.


print("Welcome to the tip calculator.\n")

# Taking all the inputs from the user and converting them to their required types
bill = float(input("What's the bill? $"))
tip_percent = int(input("What percentage tip would you like to pay? 10, 12 or 15? "))
people = int(input("How many people are splitting the bill? "))

# Calculating tip amount
tip_amt = bill * (tip_percent / 100)
total_bill = bill + tip_amt
split_bill = total_bill/people
#final_bill = round(split_bill, 2)
final_bill="{:.2f}".format(split_bill)
print("\n*******************************\n")
print(f"Split between {people} people, each person has to pay: ${final_bill}")
print("\n*********************************")