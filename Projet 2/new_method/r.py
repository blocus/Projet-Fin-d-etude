#! /usr/bin/python
from random import *
HAMMING = [
	0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
	1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
	1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
	2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
	1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
	2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
	2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
	3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
	1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
	2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
	2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
	3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
	2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
	3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
	3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
	4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8
]

def computeCost(K, sbox):
	n = len(K)
	costMin = 0xffffffffffffffff
	mMin = -1
	m = 1
	while m < 256:
		bKO = 0
		hList = []
		for k in K:
			hList.append(HAMMING[sbox[m^k]])
		hCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]
		for h in hList:
			hCount[h] += 1
		if max(hCount) < n :
			cost = 0
			reserve = n
			reserve -= hCount.count(1)
			cost += 2*hCount.count(2)
			reserve -= 2*hCount.count(2)
			for h in range(9):
				if hCount[h] >= 3:
					if (cost + reserve) < costMin:
						K_tmp = []
						for k in K:
							if HAMMING[sbox[m^k]] == h:
								K_tmp.append(k)
						cost += computeCost(K_tmp, sbox)[0];
						reserve -= hCount[h]
					else:
						bKO = 1
						break
			if bKO == 0:
				if reserve != 0:
					print "error"
				if cost < costMin:
					mMin = m
					costMin = cost
					if costMin == 0:
						break
		m += 1
	return n + costMin, mMin


def calc_moy(sbox, A):
	moy = 0.0
	for k_t in range(256):
		K = list(range(256))
		first = 1
		messages = []
		while len(K) != 1:
			if first:
				m = 0
				first = 0
			else:
				m = computeCost(K, sbox)[1]
			K_tmp = []
			y = HAMMING[sbox[m^k_t]]
			for a in A[y]:
				if a^m in K:
					K_tmp.append(a^m)
			K = list(K_tmp)
			messages.append(m)
		moy += len(messages)
	return moy / 256

####################################################################
f = open("aes.log", "w")
moymoy = 0
for i in range(100):
	seed = list(range(256))
	s = []
	while len(seed) != 0:
		r = choice(seed)
		seed.remove(r)
		s.append(r)
	print s
	A = [[], [], [], [], [], [], [], [], []]
	for i in range(256):
		y = HAMMING[s[i]]
		A[y].append(i)
	f.write("#"*50)
	f.write("\n")
	f.write(str(s))
	f.write("\n")
	moy = calc_moy(s, A)
	f.write(str(moy))
	f.write("\n")
	moymoy += moy
	print moy
f.close()
	
print "*"*10, moymoy/100, "*"*10







