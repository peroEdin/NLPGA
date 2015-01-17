from random import random, uniform, randint 
from math import pow



var = int(raw_input("Broj varijabli: "))
jed = int(raw_input("Broj jednadzbi: "))
nej = int(raw_input("Broj nejednadzbi:"))
dom = int(raw_input("Broj uvjeta na domenu: "))

print "Unos nejednakosti"

Nejednakosti = []

uneseno = 0
while  (uneseno < nej):

	r = raw_input()
	redak = map(float, r.split())

	Nejednakosti.append(redak)
	uneseno += 1
	
print "Unos uvjeta na domenu"

DomUvj = []

uneseno = 0
while  (uneseno < dom):

	r = raw_input()
	redak = map(float, r.split())

	DomUvj.append(redak)
	uneseno += 1


print "Unos dopustive tocke"
# nadji dopustivu tocku ili je sam unesi

Populacija = []

t = raw_input()
tocka = map(float, t.split())

Populacija = [ tocka for _ in xrange(20) ]
print "Pocetna populacija", Populacija

p_mutation = 0.5
#vjerojatnost svake mutacije zasebno ili ovako


def left ( tocka, indeks ):
	
	l = DomUvj[indeks][0]
	uvj = []

	for redak in Nejednakosti:
		suma = 0
		if (redak[indeks] < 0.0):
			for i in xrange(0,var):
				suma += redak[i]*tocka[i]

			uvj.append((redak[var] - (suma - redak[indeks]*tocka[indeks])) / redak[indeks] ) 
	
	if uvj == []:	
		return l
	else:
		return max( max(uvj), l)
		

def right ( tocka, indeks ):
	
	r = DomUvj[indeks][1]
	uvj = []

	for redak in Nejednakosti:
		suma = 0
		if (redak[indeks] > 0.0):
			for i in xrange(0,var):
				suma += redak[i]*tocka[i]

			uvj.append((redak[var] - (suma - redak[indeks]*tocka[indeks])) / redak[indeks] ) 

	if uvj == []:		
		return r
	else:		
		return min( min(uvj), r)
		
	
def domena ( tocka, indeks ):
	
	dom = []
	dom.append( left(tocka, indeks) )
	dom.append( right(tocka, indeks))
	return dom



def uniform_mutation( parent ):

	index = randint(0, len(parent)-1)

	dom = domena( parent, index)

	child = parent[:]
	child[index] = uniform( dom[0], dom[1] ) 

#	print "mutirano dijete", child
#	print "index", index, "domena", dom
	return child

def boundary_mutation ( parent ):

	index = randint(0, len(parent)-1)

	dom = domena( parent, index)
	child = parent[:]

	if( randint(0,1) == 0 ):
		child[index] = dom[0]
	else:	
		child[index] = dom[1]

	print "mutirano dijete", child
	print "index", index, "domena", dom

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

Mutirani = []
for jedinka in Populacija:
	if(random() < p_mutation):
		# izaberi random mutaciju		
		print "Izabrana jedinka za mutaciju...", jedinka
		#print "\t\t", Populacija	

		
		Mutirani.append( boundary_mutation( jedinka ) )
		
print "Lista mutiranih", Mutirani
















	

	
	
