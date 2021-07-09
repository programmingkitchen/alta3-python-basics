'''
    If line starts with # (comment), then ignore it, go to next line (continue).
    If line == 'done', then end the loop (break).
'''
print("Enter text.  If the text starts with #, then it won't be printed.")
print("Enter \"done\" to exit.")
while True:
    line = input('Enter text > ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Exit program.')
