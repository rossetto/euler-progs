#!/usr/bin/env python

uni =  {"0":"",
	"1":"one",
	"2":"two",
	"3":"three",
	"4":"four",
	"5":"five",
	"6":"six",
	"7":"seven",
	"8":"eight",
	"9":"nine"
	}

dez =  {"0":"",
	"1":{"0":"ten","1":"eleven","2":"twelve","3":"thirteen","4":"fourteen","5":"fifteen","6":"sixteen","7":"seventeen","8":"eighteen","9":"nineteen"},
	"2":"twenty",
	"3":"thirty",
	"4":"forty",
	"5":"fifty",
	"6":"sixty",
	"7":"seventy",
	"8":"eighty",
	"9":"ninety"
	}

cent = {"1":"one hundred",
	"2":"two hundred",
	"3":"three hundred",
	"4":"four hundred",
	"5":"five hundred",
	"6":"six hundred",
	"7":"seven hundred",
	"8":"eight hundred",
	"9":"nine hundred"
	}

s = "one thousand"
for i in range(1000):
	if i < 10:
		s += uni[str(i)]+" "
	elif i < 20:
		s += dez["1"][str(i)[1]]+" "
	elif i < 100:
		s += dez[str(i)[0]]+" "+uni[str(i)[1]]+" "
	else:
		dec = str(i)[1:]
		if dec == "00":
			s += cent[str(i)[0]]+" "
		elif int(dec) < 10:
			s += cent[str(i)[0]]+" and "+uni[str(int(dec))]+" "
		elif int(dec) < 20:
			s += cent[str(i)[0]]+" and "+dez["1"][str(i)[2]]+" "
		else:
			s += cent[str(i)[0]]+" and "+dez[str(i)[1]]+" "+uni[str(i)[2]]+" "
		
print len(s.replace(" ",""))
