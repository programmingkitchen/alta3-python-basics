#!/usr/bin/env python3
# open file in read mode
dnsfile = open("dnsservers.txt", "r")
# create list of lines
dnslist = dnsfile.readlines()
print(dnslist)
# loop over lines
for svr in dnslist:
    #print and end without a newline
    print(svr, end="")
    #print(svr) # This adds an extra line
# close your file
dnsfile.close()

