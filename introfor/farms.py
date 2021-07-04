#!/usr/bin/env python3

count = 0

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:
    print(str(count) + ": " +  str(farm))
    count += 1 

print()
for farm in farms:
    print(farm['name'])
    print(farm['agriculture'])
    print()

print("\n\nEnd program")



