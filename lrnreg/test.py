#!/usr/bin/env python3

'''
https://alta3.com
https://www.gutenberg.org/files/345/345-h/345-h.htm
http://www.gutenberg.org/files/98/98-0.txt
https://bing.com

'''

#!/usr/bin/env python3
import urllib.request
import re

print("Where should we search?")
url = input()
print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")

searchMe = urllib.request.urlopen(url).read().decode("utf-8")

print(searchMe)
