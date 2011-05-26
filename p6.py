#!/usr/bin/env python

s1 = 0
s2 = 0

for i in range(1,101):
	s1 += i**2
	s2 += i

diff = s2**2 - s1
print diff
