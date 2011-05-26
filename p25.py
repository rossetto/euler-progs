#!/usr/bin/env python

f1 = 1
f2 = 1

i = 2
l = 1
while l < 1000:
	t = f1 + f2
	f1 = f2
	f2 = t
	l = len(str(t))
	i += 1

print i
