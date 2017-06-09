"""
Galaxy Quest: https://utah.kattis.com/problems/utah.galaxyquest
"""

import sys

"""
Reading the input from standard input. 
"""
def main():
    data = sys.stdin.readlines()
    constants = data[0].split()
    del data[0]
    d = int(constants[0])
    k = int(constants[1])
    list = []
    for line in data:
        list.append([float(i) for i in line.split()])
    if FindMajority(list,d) == 'NO':
        print FindMajority(list,d)
    else:
        print FindMajority(list,d)[0]

"""
Majority element theorem: A list of elements is given in an array. We consider the elements one by one and
find the majority element of the whole array.
We consider the first element of the array as the majority element in the array
containing the first element only. Then we include the second element into the array, and
we compare this element with the first element. If they are equal we retain the two equal
elements as majority element else we discard both elements and we decide that there is
no majority element in the array containing the first two elements.
"""
def FindMajority(A,d):
    if len(A) == 0:
        return 'NO'
    elif len(A) == 1:
        return [1,A[0]]
    else:
        B = []
        if len(A)%2 == 0:
            for i in range(len(A)/2):
                distance = (A[i][0]-A[i+(len(A)/2)][0])**2+(A[i][1]-A[i+(len(A)/2)][1])**2
                if distance <= d**2:
                    B.append([A[i][0],A[i][1]])
                else:
                    pass
        else:
            y = [A[len(A)-1][0],A[len(A)-1][1]]
            for i in range(len(A)/2):
                distance = (A[i][0]-A[i+(len(A)/2)][0])**2+(A[i][1]-A[i+(len(A)/2)][1])**2
                if distance <= d**2:
                    B.append([A[i][0],A[i][1]])
                else:
                    pass
        x = FindMajority(B,d)
        if x == 'NO':
            if len(A)%2 == 1:
                n = 0
                for i in range(len(A)):
                    if (A[i][0]-y[0])**2+(A[i][1]-y[1])**2 <= d**2:
                        n += 1
                if n > len(A)/2:
                    return [n,y]
                else:
                    return 'NO'
            else:
                return 'NO'
        else:
            m = 0
            for i in range(len(A)):
                if (A[i][0]-x[1][0])**2+(A[i][1]-x[1][1])**2 <= d**2:
                    m += 1
            if m > len(A)/2:
                return [m,x[1]]
            else:
                return 'NO'
            
main()
