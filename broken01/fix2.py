#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ""
while (calc1 != "q"):
    print(type(calc1))
    print("\nWhat is the first operator? Or, enter q to quit: ")
    
    calc1 = input()

    # You need to fix the capitalization problem below so that the program exits 
    # here when you enter a q or a Q.   If it program doesn't exit heere after 
    # after a character is entered, then it will fail to convert the charater to a float
    # right after
    if calc1 == "q":
        break
    calc1 = float(calc1) # Can't coverat a string to a float
    print("\nWhat is the second operator? Or, enter q to quit: ")
    calc2 = input()
    if calc2 == "q":
        break
    calc2 = float(calc2)
    print("Enter an operation to perform on the two operators (+ or -): ")
    operation = input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    elif operation == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n Not a valid entry. Restarting...")

