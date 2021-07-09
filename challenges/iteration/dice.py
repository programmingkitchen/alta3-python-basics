'''
    A dice-rolling program that shows random breaking without user intervention.
'''
import random
while(True):
    num = random.randint(1, 12)

    if(num == 12):
        print("YOU ROLLED: ", str(num), "Ending Program . . . ")
        print("\n")
        break
    else:
        print("YOU ROLLED: ", str(num), "Rolling again.")

print("All done.")
