#! /usr/bin/python
import Crypto.PublicKey.RSA as RSA
import random
from time import time
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
key = RSA.importKey(txt)
d = key.d
y = (key.p - 1)*(key.q - 1)
R = 16
N = [116, 116, 116, 30, 30, 30, 20]
U = [2, 2, 2, 3, 3, 3, 4]
E = [0.08, 0.09, 0.1, 0.06, 0.07, 0.04, 0.05] 
t_start = time()
seed = 1497464440
random.seed(seed)
compteur = 5
u = U[compteur]
eb = E[compteur]
n = N[compteur]
list_traces = []
list_random = []
print eb
i = 0
while i < n:
    r = random.randint(0, 2**R)
    list_random.append(r)
    v_i = d + (y * r)
    l = len(bin(v_i)) - 2
    com_i = 0
    while com_i < l:
        if random.random() < eb:
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
error65 = 0
error63 = 0
tests_num = 0
for comp_i in range(len(list_uplet)-1):
    i = list_uplet[comp_i]
    for comp_j in range(comp_i + 1, len(list_uplet)):
        j = list_uplet[comp_j]
        s = i[1] - j[1]
        h = ham(s)
        test_rand = 0
        for t in i[0]:
            test_rand += list_random[t]
        for t in j[0]:
            test_rand -= list_random[t]
        if h < 65.9:
            if test_rand != 0:
                for t in i[0]:        
                    print list_random[t], list_traces[t]
                print "-"
                for t in j[0]:        
                    print list_random[t], list_traces[t]
                print h, test_rand
                print "-"*100
                error65 += 1
            if h < 63.6:
                if test_rand != 0 :
                    error63 += 1
print seed, time() - t_start, error65, error63
print str(seed)+"\t"+str(eb) + "\t" + str(error65) + "\t" + str(error63)