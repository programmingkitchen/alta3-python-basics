'''
    An infinite counter with a sleep function.
    
    To Run:     You must run Python in unbuffered mode for the sleep to work so that Python 
                doesn't buffer the output and print it all out at once at the end. 

            python -u counter3.py
'''
import time
count = 0

while True:
    time.sleep(1)
    print(count)
    count += 1
