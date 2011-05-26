#!/usr/bin/env python


import sys
sys.setrecursionlimit(200000)
t = open("in18.dat").read().splitlines()

percurso = []

soma = int(t[0])
def percorre(ponto):

        if ponto[0] == len(t)-1 or ponto[1] == len(t[ponto[0]].split()):# (1,640):
                return True

        myPercurso = []

        list = [ (ponto[0]+1,ponto[1]), (ponto[0]+1,ponto[1]+1) ]

	try:
		if t[list[0][0]].split()[list[0][1]] > t[list[1][0]].split()[list[1][1]]:
			myPercurso.append(list[0])
		else:
			myPercurso.append(list[1])
	except:
		pass

        if not myPercurso:
                return False

        for i in myPercurso:
                if percorre(i):
                        percurso.append(i)
                        return True


percorre((0,0))

for i in percurso:
	soma += int(t[i[0]].split()[i[1]])

print soma
