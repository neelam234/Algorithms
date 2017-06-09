
"""
Auto Sink: https://utah.kattis.com/problems/utah.galaxyquest
"""


from __future__ import generators

class priorityDictionary(dict):
    
    def __init__(self):
        
        self.__heap = []
        dict.__init__(self)

    def smallest(self):
        
        if len(self) == 0:
            raise IndexError 
        heap = self.__heap
        while heap[0][1] not in self or self[heap[0][1]] != heap[0][0]:
            lastItem = heap.pop()
            insertionPoint = 0
            while 1:
                smallChild = 2*insertionPoint+1
                if smallChild+1 < len(heap) and \
                        heap[smallChild] > heap[smallChild+1]:
                    smallChild += 1
                if smallChild >= len(heap) or lastItem <= heap[smallChild]:
                    heap[insertionPoint] = lastItem
                    break
                heap[insertionPoint] = heap[smallChild]
                insertionPoint = smallChild
        return heap[0][1]
	
    def __iter__(self):
        
        def iterfn():
            while len(self) > 0:
                x = self.smallest()
                yield x
                del self[x]
        return iterfn()
	
    def __setitem__(self,key,val):
        
        dict.__setitem__(self,key,val)
        heap = self.__heap
        if len(heap) > 2 * len(self):
            self.__heap = [(v,k) for k,v in self.iteritems()]
            self.__heap.sort()  
        else:
            newPair = (val,key)
            insertionPoint = len(heap)
            heap.append(None)
            while insertionPoint > 0 and \
                    newPair < heap[(insertionPoint-1)//2]:
                heap[insertionPoint] = heap[(insertionPoint-1)//2]
                insertionPoint = (insertionPoint-1)//2
            heap[insertionPoint] = newPair
	
    def setdefault(self,key,val):
        
        if key not in self:
            self[key] = val
        return self[key]
"""
Reading the input from standard input and writing to standard out.
Formatting it according to the requirement.
"""

import sys

def main():
    data = sys.stdin.readlines()
    n = int(data[0])
    del data[0]
    toll_dictionary = {}
    for i in range(n):
        line = data[0]
        del data[0]
        toll_dictionary[(line.split())[0]] = int((line.split())[1])
    h = int(data[0])
    del data[0]
    edge_start = []
    edge_end = []
    for i in range(h):
        line = data[0]
        del data[0]
        edge_start.append((line.split())[0])
        edge_end.append((line.split())[1])
    t = int(data[0])
    del data[0]
    trip_start = []
    trip_end = []
    for i in range(t):
        line = data[0]
        del data[0]
        trip_start.append((line.split())[0])
        trip_end.append((line.split())[1])
    graph_dictionary = {}
    for i in range(h):
        graph_dictionary[edge_start[i]] = {}
    for i in range(h):
        (graph_dictionary[edge_start[i]])[edge_end[i]] = toll_dictionary[edge_end[i]]
    for key in toll_dictionary:
        if key in graph_dictionary.keys():
            (graph_dictionary[key])[key] = 0
        else:
            graph_dictionary[key] = {}
            (graph_dictionary[key])[key] = 0
    for i in range(t):
        try:
            route = ShortestPath(graph_dictionary, trip_start[i], trip_end[i])
            sum = 0
            for i in range(len(route)):
                sum += toll_dictionary[route[i]]
            sum -= toll_dictionary[route[0]]
            print sum
        except KeyError:
            print 'NO'
        
"""
Dijkstra's Algorithm: Dijkstra's algorithm is an algorithm for finding the shortest 
					  paths between nodes in a graph, which may represent, 
					  for example, road networks. 
This algorithm is implemented using priority dictonary.
"""
def Dijkstra(G,start,end=None):
	
	D = {}	
	P = {}	
	Q = priorityDictionary()   
	Q[start] = 0
	
	for v in Q:
		D[v] = Q[v]
		if v == end: break
		
		for w in G[v]:
			vwLength = D[v] + G[v][w]
			if w in D:
				if vwLength < D[w]:
					raise ValueError
			elif w not in Q or vwLength < Q[w]:
				Q[w] = vwLength
				P[w] = v
	return (D,P)

"""
finding the shortest path using Dijkstra Algorithm.
"""
			
def ShortestPath(G,start,end):

	D,P = Dijkstra(G,start,end)
	Path = []
	while 1:
		Path.append(end)
		if end == start: break
		end = P[end]
	Path.reverse()
	return Path
    
main()
