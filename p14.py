#!/usr/bin/env python

llist = 0
for i in range(1,1000000):
	j = i
	list = [j]
	while j != 1:
		if j%2 == 0:
			j = j/2
			list.append(j)
		else:
			j = 3*j+1
			list.append(j)
	if len(list) > llist:
		llist = len(list)
		mx = i

print mx
