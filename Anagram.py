import sys

# txt_file = open(sys.stdin.read(),"r")

txt_file = open ("cs4150-1.txt","r")
lines = txt_file.readlines()
x,y=split lines[0]
print x,y
"""
sorted_list = [" ".join(sorted(line)) for line in lines]
#print sorted_list


anagram_list = []
for i in range(len(sorted_list)):
	
  	for j in range(i + 1, len(sorted_list)):
  	 if (sorted_list[i] == sorted_list[j]):
  	 	anagram_list.append(sorted_list[j])
  		continue
#print anagram_list
       	 
non_anagram = set(sorted_list).difference(anagram_list)
print len(non_anagram)
"""
        	
	
        		
	
	
	










