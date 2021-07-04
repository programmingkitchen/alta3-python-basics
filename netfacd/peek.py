#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())
print(netifaces.AF_LINK)
print(netifaces.ifaddresses('ens3')) 

