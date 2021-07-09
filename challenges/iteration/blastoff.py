"""
    Blast off program
    This loop counts from 10 down to 1.  When it reaches 0, then
    the condition is no longer true (n is not greater than 0),
    so the program exits the loop and the moves on to the next line
    outside of the block.
"""

count = 10
while count > 0:
    print(count)
    count = count - 1

print('Blastoff!')
