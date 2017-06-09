"""
Anagram: https://utah.kattis.com/problems/utah.anagram
"""

import sys
import time

"""
Reading input from standard in and writting it to standard out. Program to check if the
given list of words are anagrams or not.
"""
txt_file = sys.stdin
lines = txt_file.readlines()
x=lines[0].split(' ')
del lines[0]
anagram_list = {}
start_time= time.time()
sorted_list = ["".join(sorted(line.strip())) for line in lines if len(line) > 1]

for item in sorted_list:
    if item not in anagram_list:
        anagram_list[item] =1
    else:
        anagram_list[item] +=1
count=0
for key in anagram_list:
	if anagram_list[key]==1:
	   count +=1
print count
stop_time= time.time()
time_taken = stop_time - start_time
print time_taken
