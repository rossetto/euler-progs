#!/usr/bin/env python

p = [2,3,5,7,11,13,17,19]
n = 1
for i in range(1,21):
	if n%i != 0:
		for j in p:
			if i%j == 0:
				n = n*j
				break
	
print n
