"""
Cryptographer's Conundrum :https://utah.kattis.com/problems/conundrum
"""

import fileinput

for line in fileinput.input():
    days = 0
    for i in range(len(line)):
        if line[i:i+1] == "\n":
            continue
        elif (i+1) % 3 == 1 and line[i:i+1] not in "P":
            days += 1
        elif (i+1) % 3 == 2 and line[i:i+1] not in "E":
            days += 1
        elif (i+1) % 3 == 0 and line[i:i+1] not in "R":
            days += 1
    print(days)