"""
Ceiling function: https://utah.kattis.com/problems/ceiling
"""

import sys
		
def same_shape(list1,list2):
    if len(list1) == 0 and len(list2) == 0:
        return True
    elif len(list1) == 1 and len(list2) == 1: 
        return True
    elif len(list1) == 0 and len(list2) == 1:
        return False
    elif len(list1) == 1 and len(list2) == 0:
        return False
    else:
        list_1_left = []
        list_1_right = []
        list_2_left = []
        list_2_right = []
        for i in range(len(list1)):
            if list1[i] < list1[0]:
                list1_left.append(list1[i])
            elif list1[i] > list1[0]:
                list_1_right.append(list1[i])
            else:
                pass
        for i in range(len(list2)):
            if list2[i] < list2[0]:
                list_2_left.append(list2[i])
            elif list2[i] > list2[0]:
                list_2_right.append(list_2[i])
            else:
                pass
        if same_shape(list_1_left,list_2_left) and same_shape(list_1_right,list_2_right):
            return True
        else:
            return False
            
            
data = sys.stdin.readlines()
string = data[0]
del data[0]
list = []
for line in data:
    list.append([int(i) for i in line.split()])
s = []
r = []
for item in list:
    flag = False
    if len(s) == 0:
        s.append(item)
    else:
        for j in range(len(s)):
            if same_shape(item, s[j]):
                flag = True
        if flag:
            r.append(item)
        else:
            s.append(item)
print len(s)