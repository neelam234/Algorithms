"""
Erase Securely: https://utah.kattis.com/problems/erase
"""

from sys import stdin

n = int(stdin.readline())
string1 = list(stdin.readline())
string2 = list(stdin.readline())

for t in range(n):
    for i in range(len(string1)-1):
        if string1[i] == '1':
            string1[i] = '0'
        else:
            string1[i] = '1'
if string1 == string2:
    print("Deletion succeeded")
else:
    print("Deletion failed")

