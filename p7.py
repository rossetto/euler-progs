#!usr/bin/env python

fprimes = [2]
i = 3
while len(fprimes) < 10001:
	t = False
	for prime in fprimes:
		if i%prime == 0:
			t=True
			break
	if not t:
		fprimes.append(i)
	i += 2
print fprimes[-1]
