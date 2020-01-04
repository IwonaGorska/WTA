import numpy as np
import random
import math
import csv

number_of_dimensions = 2

def init_similarity_vector(number_of_elements, similarity_Dict):
    for i in range(0, number_of_elements):
    	similarity_Dict.append((i, 0))

def init_lector_vector(index_of_group, number_of_elements, min_value_lector, max_value_lector, lector_vector):
	print("Index of group: " + str(index_of_group))
	for element in range (0, number_of_dimensions):
		lector_vector.append(random.uniform(min_value_lector, max_value_lector))
		print("x[" + str(element) + "]= "+ str(lector_vector[element]))

def init_weight_vector(index_of_group, number_of_elements, min_value_weight, max_value_weight, weight_vector):
	for element in range (0, number_of_elements):
		row = []
		for r in range (0, number_of_dimensions):
			row.append(random.uniform(min_value_weight, max_value_weight))
		weight_vector.append(row)
	print(weight_vector)
	print_weights(index_of_group, number_of_elements, weight_vector)

def print_weights(index_of_group, number_of_elements, weight_vector):
	print("Index of group: " + str(index_of_group))
	for i in range (0, number_of_elements):
		for j in range (0, number_of_dimensions):
			print("w[" + str(i) + ", " + str(j) + "] = " + str(weight_vector[i][j]))

def give_key(val):
    return val[1]

def check_similarity(index_of_group, number_of_elements, similarity_Dict, lector_vector, weight_vector):
	index_of_winner = 0
	# euklides
	# For each neuron count the similarity
	for i in range (0, number_of_elements):
    	# Sum up squared differences 
		sum = 0
		for j in range (0, number_of_dimensions):
			sum = sum + (lector_vector[j] - weight_vector[i][j])**2
		similarity_Dict[i] = (i, math.sqrt(sum))
	
	# sort the dictionary with similarity
	similarity_Dict.sort(key=give_key)
	print(similarity_Dict)
	print(similarity_Dict[0][0])
	index_of_winner = similarity_Dict[0][0] 
	update_weights(index_of_group, number_of_elements, index_of_winner, weight_vector, lector_vector)

def update_weights(index_of_group, number_of_elements, index_of_winner, weight_vector, lector_vector):
	eta = 0.2
	for i in range (0, number_of_dimensions):
		old_weight = weight_vector[index_of_winner][i]
		weight_vector[index_of_winner][i] = old_weight + eta * (lector_vector[i] - old_weight)
	print("\nWeights in next iteration:")
	print_weights(index_of_group, number_of_elements, weight_vector)

def compute(i, n, mivl, mavl, mivw, mavw):
	lector_vector = []
	weight_vector = []
	similarity_Dict = []
	number_of_elements = n
	# similarity_vector = []
	# weight_vector = [[0 for col in range(4)] for row in range(4)]
	min_value_lector = mivl
	max_value_lector = mavl
	min_value_weight = mivw
	max_value_weight = mavw
	index_of_group = i
	init_similarity_vector(number_of_elements, similarity_Dict)
	init_lector_vector(index_of_group, number_of_elements, min_value_lector, max_value_lector, lector_vector)
	init_weight_vector(index_of_group, number_of_elements, min_value_weight, max_value_weight, weight_vector)
	iterations = 10
	typeLector = 'lector' + str(i)
	typeGroup = 'group' + str(i)
	for i in range (0, iterations):
		check_similarity(index_of_group, number_of_elements, similarity_Dict, lector_vector, weight_vector)
	
	with open('wtaData.csv', 'a', newline='') as csvfile:
		fieldnames = ['x', 'y', 'type']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
		if(index_of_group == 0):#you can simply return adding header to all series of data - each group - 
			#by deleting this condition, I think it's more proffesional to keep it only for first group
			writer.writeheader()
		for i in range (0, number_of_elements): 
			x = str(weight_vector[i][0]).replace('.', ',')
			y = str(weight_vector[i][1]).replace('.', ',')
			print("\nYYY " + y)
			writer.writerow({'x': x, 'y': y, 'type': typeGroup})
		xLector = str(lector_vector[0]).replace('.', ',')
		yLector = str(lector_vector[1]).replace('.', ',')
		writer.writerow({'x': xLector, 'y': yLector, 'type': typeLector})

if __name__ == '__main__':
    #I have these values common for all groups:
	number_of_elements = 10
	min_value_lector = 1
	max_value_lector = 5
	min_value_weight = 1
	max_value_weight = 5
	number_of_groups = 5
	#I can change these values and put sth different in next compute function if I want in the future
	for i in range (0, number_of_groups):
		compute(i, number_of_elements, min_value_lector, max_value_lector, min_value_weight, max_value_weight)
		min_value_lector = min_value_lector + 5
		max_value_lector = max_value_lector + 5
		min_value_weight = min_value_weight + 5
		max_value_weight = max_value_weight + 5

