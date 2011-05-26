#!/usr/bin/env python

pal = 0
for i in range(999,0,-1):
	for j in range(999,0,-1):
		if i*j < pal:
			break
		n = str(i * j)
		if len(n)%2 == 0:
			n1 = n[:len(n)/2]
			n2 = n[len(n)/2:][-1::-1]
		else:
			n1 = n[:len(n)//2]
			n2 = n[1+len(n)/2:][-1::-1]
		if n1 == n2 and int(n) > pal:
			pal = int(n)
	
print pal		
