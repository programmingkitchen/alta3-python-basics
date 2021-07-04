#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)

# This uses an extend so that each element (numbers) in the list gets iterated and added
# as in individual item in the list
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)

# Here we use append so rather than iternate, we get the entire list proto2, added
# as a single list element (no iteration).
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

