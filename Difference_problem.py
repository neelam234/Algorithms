"""
A Different Problem :https://utah.kattis.com/problems/different
"""

import sys
    
numbers = sys.stdin.readlines()
for i in numbers:
    a= i.split(' ')
    y= int(a[0])
    z= int(a[1])
    result= abs(y-z)
    print (result)
    
    
    