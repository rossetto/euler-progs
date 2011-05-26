#!usr/bin/env python

n = 600851475143

fprimes = []
i = 3
while i <= n:
	if n%i == 0:
		n = n/i
		fprimes.append(i)
		print i,n
	i += 2

print fprimes
