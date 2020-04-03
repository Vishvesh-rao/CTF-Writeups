from gmpy import *

def fermats_atk(n):

	a = root(n,2)[0]
	b = a*a - n

	while(not(is_square(b))):
		a = a+1
		b = a*a - n

	p,q = a-root(b,2)[0],a+root(b,2)[0]        # x = (q-p)/2 , y = (p+q)/2  n = (x-y)*(x+y)

	assert(p*q == n)
	return p,q


def CRT_attack(n1,n2,n3,n4,c1,c2,c3,c4,e):

	N = (n1*n2*n3*n4)

	x1 = N/n1
	x2 = N/n2
	x3 = N/n3
	x4 = N/n4

	y1 = invert(x1,n1)
	y2 = invert(x2,n2)
	y3 = invert(x3,n3)
	y4 = invert(x4,n4)

	encrypt_mesg = ((c1*x1*y1 + c2*x2*y2 + c3*x3*y3 + c4*x4*y4)%N)
	
	return root(encrypt_mesg,4)[0]
