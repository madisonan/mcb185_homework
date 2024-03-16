# authors: Madison An and Jaime Young

import gzip
import sys
import mcb185

in_cds = False
gene = []
gbff = sys.argv[1]
with gzip.open(gbff, 'rt') as fp:
	for line in fp:
		words = line.split()
		if line.startswith('ACCESSION'):
			ac = words[1]
		if line.startswith('DEFINITION'):
			sp = line.split('DEFINITION')
			if len(sp) > 1:
				defi = sp[1].strip()
		if line.startswith('ORIGIN'):
			in_cds = True
		elif in_cds:
			line = line.split()
			for seq in line[1:]:
				gene.append(seq)
	genome = ''.join(gene)

kozak_seq = []
for i in range(14):
	kozak_seq.append( {'a': 0, 'c': 0, 'g': 0, 't': 0} )

coord = []
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[0] == 'CDS':
			if 'join' in line: continue
			elif 'complement' in line:
				start = line.find('(') + 1
				stop = line.find(')')	
				beg_str = line[start:stop].split('..')[0]
				end_str = line[start:stop].split('..')[1]
				beg, end = int(beg_str), int(end_str)
				coord.append((beg, end, True))
			elif 'complement' not in line:
				beg_str = line.split()[1].split('..')[0]
				end_str = line.split()[1].split('..')[1]
				beg, end = int(beg_str), int(end_str)
				coord.append((beg, end, False))

for beg, end, is_neg in coord:
	kozak = genome[beg-10:beg+4]
	if is_neg:
		kozak = mcb185.anti_seq(genome[end-5:end+9])
	else:
		kozak = genome[beg-10:beg+4]
	
	for i, nt in enumerate(kozak):
		kozak_seq[i][nt] += 1

print('AC', ac)
print('XX')
print('ID', 'ECKOZ')
print('XX')
print('DE', defi)
print(f'{'PO':<8}', end = '')

for letter in 'ACGT':
	print(f'{letter:<10}', end = '')
print()

for i, nuc in enumerate(kozak_seq):
	print(f'{i+1:<8}', end='')
	for nt, count in nuc.items():
		print(f'{count:<8}', end='  ')
	print()
	
print('XX')