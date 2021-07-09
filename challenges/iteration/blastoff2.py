'''
    blastoff2.py
'''

count = 0
end_value = 20

'''
    Print the values all on one line separated by a space.
'''
while count < end_value:
    print(count, end=" ")
    count += 1
print("\nThe FIRST loop has ended.")
print("\n\n")

'''
    Reset the variables.
    Print the values on a separate line.
'''
count = 0
end_value = 10
while count < end_value:
    print(count)
    count += 1
print("\nThe SECOND loop has ended.")

