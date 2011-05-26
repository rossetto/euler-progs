#!/usr/bin/env python

ind = 0
for i in range(10):
	jl = range(10)
	jl.remove(i)
	for j in jl:
		jl = range(10)
		jl.remove(j)
		for k in jl:
			jl = range(10)
			jl.remove(k)
			for l in jl:
				jl = range(10)
				jl.remove(l)
				for m in jl:
					jl = range(10)
					jl.remove(m)
					for n in jl:
						jl = range(10)
						jl.remove(n)
						for o in jl:
							jl = range(10)
							jl.remove(o)
							for p in jl:
								jl = range(10)
								jl.remove(p)
								for q in jl:
									jl = range(10)
									jl.remove(q)
									for r in jl:
										if i not in [j,k,l,m,n,o,p,q,r] and j not in [i,k,l,m,n,o,p,q,r] and k not in [j,i,l,m,n,o,p,q,r] and l not in [j,k,i,m,n,o,p,q,r] and m not in [j,k,l,i,n,o,p,q,r] and n not in [j,k,l,m,i,o,p,q,r] and o not in [j,k,l,m,n,i,p,q,r] and p not in [j,k,l,m,n,o,i,q,r] and q not in [j,k,l,m,n,o,p,i,r] and r not in [j,k,l,m,n,o,p,i,q]:
											ind += 1
											if ind%10000 == 0:
												print ind, str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q)+str(r)
											if ind == 1000000:
												print "\n\n", str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)+str(q)+str(r)
												exit()
