#!/usr/bin/env python

j = 1
t = 0
d = 0
while d < 500:
	d = 0
	t = 0
	for i in range(1,j+1):
		t += i
	for i in range(1,t/2):
		if t%i == 0:
			d += 1
	print t, d
	j += 1	
