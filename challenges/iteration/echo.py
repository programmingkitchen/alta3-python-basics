'''
    Basic program for entering in text or numbers in an infinite loop.
    The text entered will be echoed back.
'''

print("Enter text at the prompt.  Enter 'done' to stop.")
while True:
    line = input('Enter text (Enter \'done\' to exit)> ')
    if line == 'done' :
        break
    print("YOU ENTERED: ", str(line))

print('\nExiting program!')
 