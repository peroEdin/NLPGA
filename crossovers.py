import random

def a_crossover(parent1, parent2):
	a = random.random()
#	print "parameter a", a
	num_variables = len(parent1)
	child1 = [ 0.0 for _ in xrange(num_variables)] 
	child2 = [ 0.0 for _ in xrange(num_variables)]
	for i in xrange(num_variables):
		child1[i] = a * parent1[i] + (1-a) * parent2[i]
		child2[i] = (1-a) * parent1[i] + a * parent2[i]

	return child1, child2

def s_crossover(parent1, parent2, k):
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

def h_crossover(parent1, parent2):
#chech if we get feasible child
	num_variables = len(parent1)
	r = random.random()
	child = [ 0.0 for _ in xrange(num_variables)]
 	for i in xrange(num_variables):
		child[i] = r * (parent2[i] - parent1[i]) + parent2[i]

	return child


if __name__ == "__main__":
#initial population
	pop_size = 10
			#num_variables = 2
	individual = [1.1, 1.1]
	population = [[0.0,0.0]] * pop_size
	for i in xrange(pop_size):
		population[i] = individual

	population[0] = [0.0, 0.0]
	print "Initial population", population

	a_offsprings = a_crossover(population[0], population[1])
	print "arithmetical offsprings", a_offsprings

	h_offsprings = h_crossover(population[0], population[1])
	print "heuristics offsprings", h_offsprings

	s_offsprings = s_crossover(population[0], population[1], 1)
	print "s_offsprings", s_offsprings
