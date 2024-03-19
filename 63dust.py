# author: Madison An

# huge number of meaningless alignments = under entropy threshold
# convert low-complexity regions to 'N' in the output

import sys
import mcb185
import dogma

w = int(sys.argv[2])
h_min = float(sys.argv[3])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline)	
	m = list(seq)
	for i in range(len(seq) -w +1):
		window = seq[i:i+w]
		A = window.count('A')
		C = window.count('C')
		G = window.count('G')
		T = window.count('T')
		h = dogma.entropy(A, C, G, T)
		if h >= h_min:
			continue
		else:
			for j in range(i, i+w):
				m[j] = 'N'
	mseq = ''.join(m)
	for i in range(0, len(mseq), 60):
		print(mseq[i:i+60])