"""
Number theory: https://utah.kattis.com/problems/utah.numbertheory
"""

import sys 

def gcd(a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
         
def isprime(x):
	prime = False
	if x >1:
		prime = True
		k = 2
		n = x ** 0.5
		while k<=n and prime == True:
			if x%k == 0:
				prime = False
			k +=1
	return prime

def exp(x,e,m):
	X=x
	E=e
	Y=1
	while E>0:
		if E % 2 == 0:
			X= (X*X)%m
			E =E/2
		else:
			Y = (X*Y)%m
			E=E-1
	return Y


def inverse(a, b):
	i = b 
	v = 0
	d = 1
	if (gcd(a,b) !=1):
		return "none"
	while  a > 0:
		t =i/a
		x = a
		a = i% x
		i=x
		x=d
		d = v-t*x
		v=x
	v %= b
	if(v < 0):
		v = (v+b) % b;
	return v	
    	   
def key(p,q):
	N= p*q
	fi = (p-1)*(q-1)	
	for i in range(2,fi):
		if (gcd(i,fi) == 1):
			e=i;
			break;	
	d = inverse(e,fi)
	print N,e,d
	                   
txt_file = sys.stdin
lines = txt_file.readlines()
for line in lines:
	words = line.split()
	if (words[0] == "gcd"):
		result = gcd(int(words[1]),int(words[2]))
		print result
		
	elif(words[0] == "isprime"):
		result = isprime(int(words[1]))
		if result:
			print "yes"
		else:
			print "no"			
	elif(words[0] == "exp"):
		result = exp(int(words[1]),int(words[2]),int(words[3]))
		print result
	
	elif(words[0] == "inverse"):
		result = inverse(int(words[1]),int(words[2]))
		print result

	elif (words[0] == "key"): 
		key(int(words[1]),int(words[2]))
		
		
	


	