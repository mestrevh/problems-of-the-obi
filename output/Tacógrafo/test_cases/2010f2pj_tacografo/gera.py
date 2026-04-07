from random import *
import sys

max_n = int(sys.argv[1])

n = randint(1,max_n)

print n

for i in xrange(n):
	a = randint(1,100)
	b = randint(0,120)
	if randint(1,5) == 4:
		b = 0
	print a, b


