#! /usr/bin/python
import Crypto.PublicKey.RSA as RSA
from random import randint, random
from math import sqrt
txt = """-----BEGIN RSA PRIVATE KEY-----
MIGrAgEAAiEAwI4/FTS6LXcAIaOLhjnHBcadAMZ3vNX35LACPliSyYMCAwEAAQIh
AJv1WoC5gSX74X5dcU+ZEmliUeyy/ErzhYRnvb6HNrapAhEA5eLMWHodVcDGYydt
LzqwbwIRANZt3URtflIcmlULDbZRmi0CEE12820NGT2ATFm1O3Gi0TkCEQClapmA
GSuSsogIRP+t/yN9AhALZOxCmVTANv/VKIsSD9m0
-----END RSA PRIVATE KEY-----"""
HAMMING = [
	(0, 0, 0), (1, 0, 0), (1, 0, 0), (2, 0, 0), (1, 0, 0), (2, 0, 0), (2, 0, 0), (2, 0, 0),
	(1, 0, 0), (2, 0, 0), (2, 0, 0), (3, 0, 0), (2, 0, 0), (3, 0, 0), (2, 0, 0), (2, 0, 0),
	(1, 0, 0), (2, 0, 0), (2, 0, 0), (3, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (3, 0, 0),
	(2, 0, 0), (3, 0, 0), (3, 0, 0), (3, 0, 0), (2, 0, 0), (3, 0, 0), (2, 0, 0), (2, 0, 0),
	(1, 0, 0), (2, 0, 0), (2, 0, 0), (3, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (3, 0, 0),
	(2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (3, 0, 0), (4, 0, 0), (3, 0, 0), (3, 0, 0),
	(2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (3, 0, 0), (4, 0, 0), (3, 0, 0), (3, 0, 0),
	(2, 0, 0), (3, 0, 0), (3, 0, 0), (3, 0, 0), (2, 0, 0), (3, 0, 0), (2, 0, 0), (2, 0, 0),
	(1, 0, 0), (2, 0, 0), (2, 0, 0), (3, 0, 0), (2, 0, 0), (3, 0, 0), (3, 0, 0), (3, 0, 0),
	(2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (3, 0, 0), (4, 0, 0), (3, 0, 0), (3, 0, 0),
	(2, 0, 0), (3, 0, 0), (3, 0, 0), (4, 0, 0), (3, 0, 0), (4, 0, 0), (4, 0, 1), (4, 0, 1),
	(3, 0, 1), (4, 0, 1), (4, 0, 1), (4, 0, 1), (3, 0, 1), (4, 0, 1), (3, 0, 1), (3, 0, 1),
	(2, 0, 1), (3, 0, 1), (3, 0, 1), (4, 0, 1), (3, 0, 1), (4, 0, 1), (4, 0, 1), (4, 0, 1),
	(3, 0, 1), (4, 0, 1), (4, 0, 1), (4, 0, 1), (3, 0, 1), (4, 0, 1), (3, 0, 1), (3, 0, 1),
	(2, 0, 1), (3, 0, 1), (3, 0, 1), (4, 0, 1), (3, 0, 1), (4, 0, 1), (3, 0, 1), (3, 0, 1),
	(2, 0, 1), (3, 0, 1), (3, 0, 1), (3, 0, 1), (2, 0, 1), (3, 0, 1), (2, 0, 1), (2, 0, 1),
	(1, 0, 1), (2, 0, 1), (2, 0, 1), (3, 0, 1), (2, 0, 1), (3, 0, 1), (3, 0, 1), (3, 0, 1),
	(2, 0, 1), (3, 0, 1), (3, 0, 1), (4, 0, 1), (3, 0, 1), (4, 0, 1), (3, 0, 1), (3, 0, 1),
	(2, 0, 1), (3, 0, 1), (3, 0, 1), (4, 0, 1), (3, 0, 1), (4, 0, 1), (4, 0, 1), (4, 0, 1),
	(3, 0, 1), (4, 0, 1), (4, 0, 1), (4, 0, 1), (3, 0, 1), (4, 0, 1), (3, 0, 1), (3, 0, 1),
	(2, 0, 1), (3, 0, 1), (3, 0, 1), (4, 0, 1), (3, 0, 1), (4, 0, 1), (4, 0, 1), (4, 0, 1),
	(3, 0, 1), (4, 0, 1), (4, 0, 1), (4, 1, 0), (3, 1, 0), (4, 1, 0), (3, 1, 0), (3, 1, 0),
	(2, 1, 0), (3, 1, 0), (3, 1, 0), (4, 1, 0), (3, 1, 0), (4, 1, 0), (3, 1, 0), (3, 1, 0),
	(2, 1, 0), (3, 1, 0), (3, 1, 0), (3, 1, 0), (2, 1, 0), (3, 1, 0), (2, 1, 0), (2, 1, 0),
	(1, 1, 0), (2, 1, 0), (2, 1, 0), (3, 1, 0), (2, 1, 0), (3, 1, 0), (3, 1, 0), (3, 1, 0),
	(2, 1, 0), (3, 1, 0), (3, 1, 0), (4, 1, 0), (3, 1, 0), (4, 1, 0), (3, 1, 0), (3, 1, 0),
	(2, 1, 0), (3, 1, 0), (3, 1, 0), (4, 1, 0), (3, 1, 0), (4, 1, 0), (3, 1, 0), (3, 1, 0),
	(2, 1, 0), (3, 1, 0), (3, 1, 0), (3, 1, 0), (2, 1, 0), (3, 1, 0), (2, 1, 0), (2, 1, 0),
	(1, 1, 0), (2, 1, 0), (2, 1, 0), (3, 1, 0), (2, 1, 0), (3, 1, 0), (3, 1, 0), (3, 1, 0),
	(2, 1, 0), (3, 1, 0), (3, 1, 0), (3, 1, 0), (2, 1, 0), (3, 1, 0), (2, 1, 0), (2, 1, 0),
	(1, 1, 0), (2, 1, 0), (2, 1, 0), (3, 1, 0), (2, 1, 0), (3, 1, 0), (2, 1, 0), (2, 1, 0),
	(1, 1, 0), (2, 1, 0), (2, 1, 0), (2, 1, 0), (1, 1, 0), (2, 1, 0), (1, 1, 0), (1, 1, 0),
	(0, 1, 0)
]
def ham(a):
	if a < 0:
		a = 0 - a
	h = 0
	l = []
	tmp = (0, 0, 0)
	old_naf = 0
	t = 0
	while a != 0:
		a += tmp[1]
		p = a & 0xff
		if (tmp[1] == 0 and old_naf == 1 and p % 2 == 1):
			p += 1
		tmp = HAMMING[p]
		old_naf = tmp[2]
		h += tmp[0]
		a >>= 8
	if tmp[1] == 1:
		h += 1
	return h
f = open("attack.log", "w")
key = RSA.importKey(txt)
d = key.d
y = (key.p - 1)*(key.q - 1)
R = 16
N = [116, 116, 116, 30, 30, 30, 20]
U = [2, 2, 2, 3, 3, 3, 4]
E = [0.08, 0.09, 0.1, 0.06, 0.07, 0.04, 0.05]
for compteur in range(len(U)):
	u = U[compteur]
	eb = E[compteur]
	n = N[compteur]
	list_traces = []
	list_random = []
	i = 0
	while i < n:
		r = randint(0, 2**R)
		list_random.append(r)
		v_i = d + (y * r)
		l = len(bin(v_i)) - 2
		com_i = 0
		while com_i < l:
			if random() < eb:
				v_i ^= 2**com_i
			com_i += 1
		list_traces.append(v_i)
		i += 1 
	list_uplet = []
	if u == 2:
		for i in range(n-1):
			for j in range(i+1, n):
				list_uplet.append([(i, j), list_traces[i] + list_traces[j]])
	if u == 3:
		for i in range(n-2):
			for j in range(i+1, n-1):
				for k in range(j+1, n):
					list_uplet.append([(i, j, k), list_traces[i] + list_traces[j] + list_traces[k]])
	if u == 4:
		for i in range(n-3):
			for j in range(i+1, n-2):
				for k in range(j+1, n-1):
					for l in range(k+1, n):
						list_uplet.append([(i, j, k, l), list_traces[i] + list_traces[j] + list_traces[k] + list_traces[l]])
	print "recherche uplet"
	error = 0
	tests_num = 0
	for i in list_uplet:
		for j in list_uplet:
			if i[0] == j[0]:
				continue
			tests_num += 1
			s = i[1] - j[1]
			h = ham(s)
			if h < 65:
				test_rand = 0
				for t in i[0]:
					test_rand += list_random[t]
				for t in j[0]:
					test_rand -= list_random[t]
				if test_rand != 0:
					error += 1
				print i[0], j[0], test_rand
	print error
	ch = str(eb) + "\t" + str(error) + "\t" + str(tests_num) + "\n"
	f.write(ch)
				