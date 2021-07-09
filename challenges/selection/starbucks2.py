"""
    24: venti
    16: grande
    12: tall
"""

ounces = 0
size = input("Enter size (venti, grande, or tall): ")

if size == 'venti':
    ounces = 24
    print("You're drink is " + str(ounces) + " ounces!")
elif size == 'grande':
    ounces = 16
    print("You're drink is " + str(ounces) + " ounces!")
elif size == 'tall':
    ounces = 12
    print("You're drink is " + str(ounces) + " ounces!")

print("Done")
