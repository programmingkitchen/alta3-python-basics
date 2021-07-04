#!/usr/bin/env python3
## Script to search and stop on first match
import os

## Define a function that stops searching on first match
def find(name, path):
    for root, dirs, files in os.walk(path):
        print("Root: " + str(type(root))  + ": " + str(root))
        print("Dirs: " + str(type(dirs)) + ": " + str(dirs))
        print("Files: " + str(type(files)) + ": " + str(files))
        print()
        return True

name = "foo.txt"
path = "/home/student/mycode/walkingtree"
print(find(name, path))

