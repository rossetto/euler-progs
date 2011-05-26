#!/usr/bin/env python

f = open("in22.dat").read()
f = f.rstrip('"').lstrip('"').split('","')

soma = 0
f.sort()
for name in f:
	v = 0
	for c in name:
		v += (ord(c) - 64)
#	print name, f.index(name) + 1, v
	s = (f.index(name) + 1) * v
	soma += s

print soma
