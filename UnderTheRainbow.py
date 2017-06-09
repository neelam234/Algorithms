"""
Under the Rainbow: https://utah.kattis.com/problems/utah.rainbow
"""

import sys
import math

def rainbow(hotels):
    penalties = [0 if i<2 else -1 for i in range(len(hotels))]
    penalties[1] = math.pow(400 - hotels[0], 2)
    for i in range(1,len(hotels)):
        for j in range(0,i):
            tempPen = int(penalties[j] + math.pow(400 - (hotels[i] - hotels[j]), 2))            
            if (penalties[i] == -1 or tempPen < penalties[i]):
                penalties[i] = tempPen
                print (penalties)
    return penalties[i]


distance =[]
txt_file = sys.stdin
lines = txt_file.readlines()
total_hotels = lines[0]
del lines[0]
for i in lines:
	distance.append(i)
for i in range(len(distance)):
	distance[i] = int(distance[i])
#print (distance)
print(rainbow(distance))