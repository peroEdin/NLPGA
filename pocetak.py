


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
Populacija.append( [tocka] * 10 ) # populacija velicine 10



def left ( tocka, indeks ):
	
	l = DomUvj[indeks][0]
	uvj = []

	for redak in Nejednakosti:
		suma = 0
		if (redak[indeks] < 0.0):
			for i in range(0,var):
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
			for i in range(0,var):
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


print domena([0.5,1.5],1)













