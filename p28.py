#!/usr/bin/env python

p = [1]
for i in range(2,100000,2):
	n = 0
	while n < 4:
		p.append(p[-1] + i)
		n += 1
	if p[-1] == 1001*1001:
		break
print sum(p)
