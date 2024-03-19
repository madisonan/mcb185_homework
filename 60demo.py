import mcb185
import sys


# stepping through FASTA files
import mcb185
import sys

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))


# GC composition	
import mcb185
import sys
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc / len(seq))

	
# nucleotide counts
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	#name = defwords[0]
	A = 0
	C = 0
	G = 0
	T = 0
	N = 0
	for nt in seq:
		if   nt == 'A': A += 1
		elif nt == 'C': C += 1
		elif nt == 'G': G += 1
		elif nt == 'T': T += 1
		else:           N += 1
	print(A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))

"""
# indexing with str.find()
nts = 'ACGTN'
counts = [0] * len(nts)
for nt in seq:
	idx = nts.find(nt)
	counts[idx] += 1
print(name, end='\t')
for n in counts: print(f'{n/len(seq):.4f}', end='\t')
print()


# counting with str.count()
nts = 'ACGTN'
print(name, end='\t')
for nt in nts:
	print(seq.count(nt) / len(seq), end='\t')
print()


# str.replace() doens't modify old string bc strings can't be modified
def transcribe(dna):
	return dna.replace('T', 'U')	# creates new string with changes


# sliding through algorithms
w = 10
s = 1
for i in range(0, len(seq) -w +1, s):
	subseq = seq[i:i+w]
"""