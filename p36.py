#!/usr/bin/env python

def dec2bin(n):
	l = []
	while n != 1:
		d = n%2
		n = n//2
		l.append(str(d))
	l.append(str(n))
	l.reverse()
	return "".join(l)


soma = 0
for i in range(1,1000000):
	s = str(i)
	if len(s)%2 ==0:
		n1 = s[:len(s)//2]
		n2 = s[len(s)//2:][-1::-1]
		if n1 == n2:
			sb = dec2bin(i)
			if len(sb)%2 ==0:
				nb1 = sb[:len(sb)//2]
				nb2 = sb[len(sb)//2:][-1::-1]
				if nb1 == nb2:
					soma += i
			else:
				nb1 = sb[:len(sb)//2]
				nb2 = sb[1+len(sb)//2:][-1::-1]
				if nb1 == nb2:
					soma += i
	else:
		n1 = s[:len(s)//2]
		n2 = s[1+len(s)//2:][-1::-1]
		if n1 == n2:
			sb = dec2bin(i)
			if len(sb)%2 ==0:
				nb1 = sb[:len(sb)//2]
				nb2 = sb[len(sb)//2:][-1::-1]
				if nb1 == nb2:
					soma += i
			else:
				nb1 = sb[:len(sb)//2]
				nb2 = sb[1+len(sb)//2:][-1::-1]
				if nb1 == nb2:
					soma += i

print soma
