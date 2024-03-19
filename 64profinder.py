import dogma
import mcb185
import sys

# 5983

minpro = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	pro_count = 0
	for f in range(3):
		rna1 = dogma.transcribe(seq[f:])
		rna2 = dogma.transcribe(mcb185.anti_seq(seq[f:]))
		for rna in (rna1, rna2):
			trans = dogma.translate(rna)
			orfs = trans.split('*')
			for orf in orfs:
				if 'M' in orf:
					start = orf.index('M')
					protein = orf[start:]
					if len(protein) >= minpro:
						pro_count += 1
						print('>protein:', pro_count, sep='')
						print(protein)