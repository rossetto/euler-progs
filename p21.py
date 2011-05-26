#!/usr/bin/env python

soma = 0
plist = []
for i in range(1,10001):
	d = 0
	d2 = 0
	for j in range(1,1+i/2):
		if i%j == 0:
			d += j
	for j in range(1,1+d/2):
		if d%j == 0:
			d2 += j
	if d2 == i and d != i and i not in plist:
		print i, d
		plist.append(i)
		plist.append(d)

print sum(plist)
