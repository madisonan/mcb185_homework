# author: Madison An (went over in class but changed slightly from that)

# finds and reports first instance of missing kmers

import sys
import mcb185
import itertools

fasta = sys.argv[1]
no_kmer = 0
k = 1
while no_kmer == 0:
	print('checking', k)
	k = k+1
	
	# get all kmers for all sequences
	kcount = {}
	for defline, seq in mcb185.read_fasta(fasta):
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
			
	antiseq = mcb185.anti_seq(seq)
	for i in range(len(antiseq) -k +1):
		kmer = antiseq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1

	# check all kmers against all possible kmers
	if len(kcount.keys()) == 4**k: continue
	
	# report missing kmers
	for ktup in itertools.product('ACGT', repeat=k):
		kmer = ''.join(ktup)
		if kmer not in kcount: 
			no_kmer += 1
			print(kmer)
