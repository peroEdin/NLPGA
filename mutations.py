from random import random, uniform, randint 
from math import pow
from sys import argv
from input import input, initialize_population


def left ( point, index, Domain_rest, Eq_rest, Ieq_rest ):
	
	l = Domain_rest[index][0]
	restrictions = []
	var = len(point)

	for row in Ieq_rest:
		suma = 0
		if (row[index] < 0.0):
			for i in xrange(0,var):
				suma += row[i]* point[i]

			restrictions.append(( row[var] - (suma - row[index]*point[index])) / row[index] ) 
	
	if restrictions == []:	
		return l
	else:
		return max( max(restrictions), l)
		

def right (  point, index, Domain_rest, Eq_rest, Ieq_rest ):

	r = Domain_rest[index][1]
	restrictions = []
	var = len(point)

	for row in Ieq_rest:
		suma = 0
		if (row[index] > 0.0):
			for i in xrange(0,var):
				suma += row[i]* point[i]

			restrictions.append(( row[var] - (suma - row[index]*point[index])) / row[index] ) 
	
	if restrictions == []:	
		return r
	else:
		return min( min(restrictions), r)
		
	
def domain ( point, index, Domain_rest, Eq_rest, Ieq_rest ):
	
	dom = []
	dom.append( left(point, index, Domain_rest, Eq_rest, Ieq_rest ))
	dom.append( right(point, index, Domain_rest, Eq_rest, Ieq_rest ))
	return dom


def uniform_mutation( parent, parent_dom, index ):

	#index = randint(0, len(parent)-1)

	#parent_dom = domena( parent, index)

	child = parent[:]
	child[index] = uniform( parent_dom[0], parent_dom[1] ) 

	#print "mutirano dijete", child
	#print "index", index, "domena", parent_dom
	return child

def boundary_mutation ( parent, parent_dom, index ):

	#index = randint(0, len(parent)-1)

	#dom = domena( parent, index)
	child = parent[:]

	if( randint(0,1) == 0 ):
		child[index] = parent_dom[0]
	else:	
		child[index] = parent_dom[1]

	#print "mutirano dijete", child
	#print "index", index, "domena", parent_dom

	return child

"""
Testiranje kada imamo simulaciju GA, tj. generacije i otkrijemo kako zadati parametar za ne-uniformnu mutaciju

def delta ( t, y):
	
	return y * uniform(0,1) * pow((1 - t/maximum_gen), nu_parameter) 
# t ~ generation_num
# nu_parameter ~ system parameter determining the degree of non-uniformity

def nonunif_mutation( parent ):

	index = randint(0, len(parent)-1)

	dom = domena( parent, index)
	child = parent[:]

	if( randint(0,1) == 0 ):
		child[index] = child[index] + delta(generation_num, dom[1] - child[index])	
	else:
		child[index] = child[index] - delta(generation_num, child[index] - dom[0])	

"""


if __name__ == "__main__":

# restrictions from file

	data = []
	data = input(argv[1])

	eq = data[1]
	ieq = data[3]
	d_restrictions = data[5]

	#print eq, ieq, d_restrictions

# find or enter feasible individual
	print "Enter feasible individual"
	tmp = raw_input()
	Population = initialize_population(tmp)
	print "Initial population", Population

	# possibility of mutation
	p_mutation = 0.5

	Mutated = []
	for individual in Population:
		if(random() < p_mutation):
			   # izaberi random mutaciju		
			   print "Individual for mutation ", individual
			   #print "\t\t", Populacija	
			   index = randint(0, len(individual)-1)
			   Ind_domain = domain( individual, index, d_restrictions, eq, ieq)
			   Mutated.append( uniform_mutation( individual, Ind_domain, index ) )    
	   		
	print "Mutated list", Mutated	
