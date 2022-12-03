from decimal import Decimal
import math
# Defining function for addition
def add(a,b):
    addition= a + b
    print(f"The value after addition is {addition}")

# Defining function for subraction
def sub(a,b):
    subraction= a - b
    print(f"The value after subtraction is {subraction}")

# Defining function for multiplication
def mul(a,b):
    multiplication= a * b
    print(f"The value after multiplication is {multiplication}")

# Defining function for division
def div(a,b):
    division= a / b
    print(f"The value after division is {division}")

# Defining function for square root 
def sq(a):
    square_root= math.sqrt(a)
    print(f"The value after square root is {square_root}")

# Providing options to the user
print("A for ADDITION")
print("B for SUBTRACTION")
print("M for MULTIPLICATION")
print("D for DIVISION")
print("S for SQUARE ROOT")
print()
print("CHOOSE YOUR OPTION")

# Asking user for input
choice = input("ENTER YOUR CHOICE: ")
if choice == "A" or choice == "a":
    print("YOU CHOSE ADDITION")
elif choice == "B" or choice == "b":
    print("YOU CHOSE SUBTRACTION")
elif choice == "M" or choice == "m":
    print("YOU CHOSE MULTIPLICATION")
elif choice == "D" or choice == "d":
    print("YOU CHOSE DIVISION")
elif choice == "S" or choice == "s":
    print("YOU CHOSE SQUARE ROOT")

# Taking values From the user and defining special condition for square root choice
if choice == "S" or choice == "s":
    print("GIVE NUMBER WHOSE SQUARE ROOT YOU WANT CALCULATE")
    a= eval(input("ENTER NUMBER: "))
else:
    a = eval(input("ENTER THE 1st NUMBER: "))
    b = eval(input("ENTER THE 2nd NUMBER: "))
   
#  Defining conditions for different choices and then Calling the functions according to the choice 
if choice == "A" or choice == "a":
    add(a,b)
elif choice == "B" or choice == "b":
    sub(a,b)
elif choice == "M" or choice == "m":
    mul(a,b)
elif choice == "D" or choice == "d":
    div(a,b)
elif choice == "S" or choice == "s":
    sq(a)
    




