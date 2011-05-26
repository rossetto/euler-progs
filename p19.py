#!/usr/bin/env python

import calendar

ns = 0
for y in range(1901,2001):
	for m in range(1,13):
		if calendar.weekday(y,m,1) == 6:
			ns += 1

print ns
