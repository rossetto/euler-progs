#!/usr/bin/env python
from pylab import *

numbers = load("in11.dat",unpack=True)

m = 0
for i in range(20):
	for j in range(20):
		p = 1
		for k in range(4):
			try:
				p *= numbers[i+k][j+k]
				out=False
			except:
				out=True
				break
		if not out:
			if p > m:
				m = p
		p = 1
		for k in range(4):
			try:
				p *= numbers[i-k][j+k]
				out=False
			except:
				out=True
				break
		if not out:
			if p > m:
				m = p
		p = 1
                for k in range(4):
                        try:
                                p *= numbers[i+k][j]
				out=False
                        except:
                                out=True
                                break
		if not out:
			if p > m:
				m = p
		p = 1
                for k in range(4):
                        try:
                                p *= numbers[i][j+k]
                                out=False
                        except:
                                out=True
                                break
		if not out:
			if p > m:
				m = p
print m
