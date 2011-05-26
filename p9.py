#!/usr/bin/env python

for i in range(1,999):
	for j in range(1,999):
		k = (i**2 + j**2)**0.5
		if int(k) == k and i+j+k == 1000:
			print i*j*k
