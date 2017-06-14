"""
Black Friday: https://utah.kattis.com/problems/blackfriday
"""

import sys

input = sys.stdin.readlines()
out = []
del_list=[]
occurs =  list(map(int,input[1].split(' ')))

for ele in occurs:
    if ele in out:
        del_list.append(ele)
        #out.remove(ele)      
    else:
        out.append(ele)

for i in del_list:
    if i in out:
        out.remove(i)
        
if len(out)==0 :
    print ("none")
else:
    s= max(out)
    for i,e in enumerate(occurs):
        if e == s:
            print (i+1)
            