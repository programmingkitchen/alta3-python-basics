'''
    A robust squaring program.
'''
print("INTEGER SQUARING PROGRAM.\n")
print("Enter an integer to square.\nEnter 'exit' when you're done.\n")

while True:
    data = input("Enter an integer(exit to end): ")
    if data == "exit":
        break
    try:
        i = int(data)
        print(i, "squared is", i * i, "\n")
    except:
        print("ERROR: you must enter an integer.\n")

print("\n\nOkay, bye!")
