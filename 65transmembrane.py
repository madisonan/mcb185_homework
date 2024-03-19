# author: Madison An

import dogma
import mcb185
import sys


# signal peptide
def sig_pep(seq):
	for i in range(0, 30 -8 +1):
		rna = seq[i:i+8]
		kd = dogma.hydropathy(rna)
		avg_kd = kd / 8
		if avg_kd >= 2.5 and 'P' not in rna:
			return True
	return False


# transmembrane region
def trans_mem(seq):
	for i in range(30, len(seq) -11 +1):
		rna = seq[i:i+11]
		kd = dogma.hydropathy(rna)
		avg_kd = kd / 11
		if avg_kd >= 2.0 and 'P' not in rna:
			return True
			#return defline
	return False


# run it
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if sig_pep(seq) and trans_mem(seq):
		print(defline[:60])


# need 468