from replit import clear
from art import logo

#Add
def add(n1,n2):
    return n1 + n2

#Subtract
def subtract(n1,n2):
    return n1 - n2

#Divide
def divide(n1,n2):
    return n1 / n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Calculator backbone
def calculate(n1,n2,symbol):
    return operations[symbol](n1,n2)

#Operations dictionary
operations = {
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply
    }
def main():
    print (logo)
    # Taking inputs from the user: 2 numbers and an operator
    num1 = float(input("What is the first number? "))

    for key in operations: 
        print (key)
    symbol = input("Which operation do you want to use? ")
    num2 = float(input("What is the second number? "))

    answer = calculate(num1,num2,symbol)
    print (f"{num1} {symbol} {num2} = {answer}")
    continue_cal = input("\nType y to continue with the answer, n to start afresh.\n1")

    while continue_cal.lower() =='y':
        old_answer = answer
        symbol = input("Which operation do you want to use? ")
        num3 = float(input("What is the next number? "))
        answer = calculate(answer,num3,symbol)

        print (f"{old_answer} {symbol} {num3} = {answer}")
        continue_cal = input("\nType y to continue with the answer, n to start afresh.\n1")
    else:
        clear()
        main()

main()