#! /usr/bin/python

def hamming_NAF(d):
	h = 0
	ch = ""
	if d != 0:
		if d < 0:
			d = 0 - d
		while d > 0:
			if d & 1 == 1:
				d_i = 2-(d%4)
				d = d - d_i
				if d_i == 1:
					ch += "+"
				elif d_i == -1:
					ch += "-"
				elif d_i == 0:
					ch += "0"
			else:
				ch += "0"
				d_i = 0
			d /= 2
			if d_i != 0:
				h += 1
	return ch[::-1], h
i = 0
l = []
while i < 0x100:
	ch, h = hamming_NAF(i)
	t = 0
	ch = "0"*(9-len(ch))+ch
	t = ch[0]
	old = ch[1]
	if t == "0":
		t = 0
	elif t == "+":
		t = 1
		h -= 1
	elif t == '-':
		t = -1
		h -= 1
	if old == "0":
		old = 0
	elif old == "+":
		old = 1
	elif old == "-":
		old = -1
	l.append((h, t, old))
	print ch, h, t
	i += 1
i = 0
while i < len(l):
	print l[i: i+8]
	i += 8