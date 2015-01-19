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
		line = line.split(' ')
		line = [int(x) for x in line]
		eq += [line]
	#print eq

	input.readline()
	for _ in xrange(num_ieq):
		line = input.readline()
		line = line.split(' ')
		line = [int(x) for x in line]
		ieq += [line]
	#print ieq

	input.readline()
	for _ in xrange(num_d_restrictions):
		line = input.readline()
		line = line.split(' ')
		line = [int(x) for x in line]
		d_restrictions += [line]
	#print d_restrictions

	input.close()
	#return data !!

if __name__ == "__main__":
	input(sys.argv[1])
