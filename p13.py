#!/usr/bin/env python

numbers = open("in13.dat").read().splitlines()

soma = 0
for n in numbers:
	soma += int(n)

print str(soma)[:10]
