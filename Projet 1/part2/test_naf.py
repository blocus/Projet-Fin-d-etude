#! /usr/bin/python
import naf
def hamming_NAF(d):
	h = 0
	if d < 0:
		d = 0 - d
	while d > 0:
		if d & 1 == 1:
			d_i = 2-(d%4)
			d = d - d_i
		else:
			d_i = 0
		d /= 2
		if d_i != 0:
			h += 1
	return h

i = 0
while i < 2**20:
	n = naf.NAF(i)
	h = n.hamming()
	i += 1
	if i % 1000 == 0:
		print i / 1000