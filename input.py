import sys


def input(file_name):
	input = open(file_name, 'r')

	#how many constraints all together
	line = input.readline()
	
	line = line.split(' ')
	num_variables = int(line[0])
	num_eq = int(line[1])
	num_ieq = int(line[2])
	num_d_restrictions = int(line[3])
	#print "num_variables ", num_variables, "num_eq", num_eq, "num_ieq", num_ieq, "d_r", num_d_restrictions

	eq = []
	ieq = []
	d_restrictions = []

	#get all constraints
	input.readline()
	for _ in xrange(num_eq):
		line = input.readline()
		new = map(float, line.split())
		eq.append(new)
	#print "EQ", eq

	input.readline()
	for _ in xrange(num_ieq):
		line = input.readline()
		new = map(float, line.split())
		ieq.append(new)
	#print "IEQ", ieq

	input.readline()
	for _ in xrange(num_d_restrictions):
		line = input.readline()
		new = map(float, line.split())
		d_restrictions.append(new)
	#print "D_REST", d_restrictions

	input.close()
	return num_eq, eq, num_ieq, ieq, num_d_restrictions, d_restrictions


if __name__ == "__main__":
	
	data = []
	data = input(sys.argv[1])
	print data
