# author: Madison An

import mcb185
import sys
import dogma
seq = sys.argv[1]
minlength = int(sys.argv[2])

def genefinder(seq, minlength):
	cords = []
	for frame in range(3):
		fseq = seq[frame:]
		i = frame

		while i < len(fseq):

			codon = fseq[i:i+3]
			if codon == 'ATG':
				start = i

				for j in range(i, len(fseq) -2, 3):
					codon = fseq[j:j+3]
					if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
						stop = j

						if len(fseq[start:stop]) >= minlength:
							cords.append((start, stop))

						i = stop
						break
			i += 3
	return cords

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	antiseq = dogma.revcomp(seq)

	for_gene = genefinder(seq, minlength)
	for nt in for_gene:
		print('+', nt[0], nt[1], '-')

	rev_gene = genefinder(antiseq, minlength)
	for nt in rev_gene:
		print('-', nt[0], nt[1], '+')