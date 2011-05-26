#!/usr/bin/env python

p = []
for i in range(2,101):
	for j in range(2,101):
		a = i**j
		if a not in p:
			p.append(a)

print len(p)
