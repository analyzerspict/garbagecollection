from random import randrange as rr
from itertools import *
import re

def get_tsp(src_dist, dist, priorities):
	
	nodes = [i + 1 for i in xrange(len(dist))] # initial ordering: 1,2,3,4,5
	
	best_dist = 10**18 # Set best dist to infinity
	best_path = [0,1,2,3,4,5,6] # Stores the best path
	
	for ordering in permutations(nodes, len(nodes)):
		#print ordering

		cur_dist = 0 # stores distance of current ordering
		
		cur_dist += src_dist[ordering[0]]

		for i in xrange(len(ordering) - 1):
			#print ordering[i], ordering[i + 1]
			# Consider that you are going from node U to node V
			# Function is: priority(u) + dist(u, v)
			cur_dist += (priorities[ordering[i] - 1] * dist[ordering[i] - 1][ordering[i + 1] - 1])
		
		cur_dist += (priorities[ordering[len(ordering) - 1] - 1] * dist[ordering[len(ordering) - 1] - 1][6])
		
		if cur_dist < best_dist: # if current permutations is better than previous best
			best_dist = cur_dist # update best distance
			best_path = ordering # update best path
	
	return (best_dist, [0] + list(best_path) + [6]) # return a tuple containing best distance and best path
	
	
	
	
def calculate_path(data,priorities):


	for i in xrange(len(data)):
		for j in xrange(len(data[i])):
			num=re.findall("[-+]?\d+[\.]?\d*",data[i][j])  #regex to eliminate the string characters from the list
			data[i][j]=float(str(num[0]))
		
	#data = [[1.0, 6.6, 7.1, 6.9, 7.2, 6.4, 6.4], [6.3, 1.0, 0.7, 0.8, 0.6, 0.6, 1.5], [7.1, 0.7, 1.0, 1.4, 1.3, 1.2, 1.4], [6.6, 0.8, 1.4, 1.0, 0.7, 0.8, 2.3], [6.9, 0.6, 1.3, 0.7, 1.0, 1.2, 2.1], [6.1, 0.6, 1.2, 0.8, 1.2, 1.0, 2.0], [6.6, 1.7, 1.4, 2.5, 2.3, 2.6, 1.0]]
	
	#priorities = [0.5, 2.0, 3.0, 4.0, 5.0]
	priorities = [1.0, 0.1, 5.0, 9.0, 9.0]
	for i in xrange(len(priorities)):
		priorities[i] = 1 / priorities[i] # inverse
	
	src_distances = data[0] # Distance of Source to all other nodes
	dst_distances = data[len(data) - 1] # Distance of destination
	
	other_distances = data[1: len(data) - 1] # Distance of nodes 1 to (n - 1)
	
	best_dist, best_path = get_tsp(src_distances, other_distances, priorities)
	
	print best_dist, best_path
	
	return best_path
	
