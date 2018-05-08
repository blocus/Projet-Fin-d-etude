#! /usr/bin/python

f = open("stat_seq_4.log", "r")


min_entro_val = ""
min_entro = 256
min_taille = 256
min_taille_val = ""
min_all = (256, 256)
min_all_val = ""




for l in f:
	l = l[:-1].split("\t")
	taille = int(l[2])
	entro = float(l[3])
	taille, entro
	if taille == min_taille:
		if int(l[1][1:]) < o:
			min_taille = taille
			min_taille_val = l[0]
			o = l[1]
	if taille < min_taille:
		min_taille = taille
		min_taille_val = l[0]
		o = l[1]
	if entro < min_entro:
		min_entro = entro
		min_entro_val = l[0]
	if entro < min_all[0] and taille < min_all[1]:
		min_all = (entro, taille)
		min_all_val = l[0]
		o1 = l[1]

print "entro ", min_entro_val, min_entro
print "taille", min_taille_val, min_taille, o
print "all   ",min_all_val, min_all, o1