#!/usr/bin/env python3
# Loop continues as long as user enters y or Y
# You have to set the value to make the loop run the first time
choice = "y"
while choice.lower() == "y":
    print("Hello!")
    choice = input("Say hello again? (y/n): ")
print("Bye!")  # runs when loop ends
