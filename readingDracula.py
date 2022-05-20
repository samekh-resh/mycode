#!/usr/bin/env python3
from pprint import pprint

with open("dracula.txt") as dracFile:
    times = 0
    for line in dracFile:
        
        if "vampire" in line.lower():
            times+=1
            with open("linesContainingVampire.txt", "a") as theFile:
                theFile.write(line + '\n')
           # pprint(line.replace('\n', ''))
print(times)


