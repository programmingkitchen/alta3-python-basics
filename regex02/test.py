#!/usr/bin/env python3
import re

mystring = "Contact: <sip:+17175664428@[2600:2304:9210:ec::2]:5060;eri-generated-at=10.172.0.132>"
print(mystring)
print()

myobj = re.search(r'sip:\+(\d+)@\[(.*)\]:?(\d+)?', mystring)
print(type(myobj))
print(myobj)
print()

print(myobj.group(0))
print(myobj.group(1))
print(myobj.group(2))
print(myobj.group(3))

