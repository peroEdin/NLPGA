from random import random
from input import input, initialize_population
from sys import argv

def a_crossover(parent1, parent2):
	a = random()
#	print "parameter a", a
	num_variables = len(parent1)
	child1 = [ 0.0 for _ in xrange(num_variables)]
	child2 = [ 0.0 for _ in xrange(num_variables)]
	for i in xrange(num_variables):
		child1[1] = a * parent1[i] + (1-a) * parent2[i]
		child2[i] = (1-a) * parent1[i] + a * parent2[i]

	return child1, child2

def s_crossover(parent1, parent2, k, eq, ieq, d_restrictions):
#chech if we get feasible child
	num_variables = len(parent1)
	child1 = [ 0.0 for _ in xrange(num_variables)] 
	child2 = [ 0.0 for _ in xrange(num_variables)]
	a = 1
	while True:
		child1 = parent1[:k] + parent2[k:]
		child2 = parent2[:k] + parent1[k:]
		if True: # true = child1 and child2 are feasible
			break
	return child1, child2

def h_crossover(parent1, parent2, eq, ieq, d_restrictions):
#chech if we get feasible child
	num_variables = len(parent1)
	r = random()
	child = [ 0.0 for _ in xrange(num_variables)]
 	for i in xrange(num_variables):
		child[i] = r * (parent2[i] - parent1[i]) + parent2[i]

	return child


if __name__ == "__main__":
#initial population

	data = []
	data = input(argv[1])
	num_variables = data[6]
	eq = data[1]
	ieq = data[3]
	d_restrictions = data[5]
	pop_size = 20
	population = initialize_population(argv[2] + ' ' + argv[3], pop_size)

	a_offsprings = a_crossover(population[0], population[1])
	print "arithmetical offsprings", a_offsprings

	s_offsprings = s_crossover(population[0], population[1], 1, eq, ieq, d_restrictions)
	print "simple offsprings", s_offsprings

	h_offsprings = h_crossover(population[0], population[1], eq, ieq, d_restrictions)
	print "heuristics offsprings", h_offsprings

