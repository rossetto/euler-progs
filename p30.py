#!/usr/bin/env python

p = []
for i in range(10,500000):
	s = 0
	for j in str(i):
		s += int(j)**5
	if s == i:
		p.append(i)

print p
