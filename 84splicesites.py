# author: Madison An (worked on in class)

import gzip
import sys
import json
import mcb185


fasta = sys.argv[1]
gff = sys.argv[2]


# function for transfac
def print_pwm(pwm, ac, id, de):
	print('AC', ac)
	print('XX')
	print('ID', id)
	print('XX')
	print('DE', de)
	print('PO', '\t A', '\t  C', '\t   G', '\t    T')
	for i, n in enumerate(pwm):
		a = n['A']
		c = n['C']
		g = n['G']
		t = n['T']
		print(f'{i+1:<8} {a:<8} {c:<8} {g:<8} {t:<8}')
	print('XX')
	print('//')


# read all the sequences into a dictionary
chrom = {}
for defline, seq in mcb185.read_fasta(fasta):
	chid = defline.split()[0]
	chrom[chid] = seq


# read all the features (introns)
introns = []
with gzip.open(gff, 'rt') as fp:
	for line in fp:
		f = line.split('\t')
		c = f[0]
		t = f[2]
		b = int(f[3]) -1
		e = int(f[4]) -1
		n = f[5]
		s = f[6]
		if n == '.': continue
		n = float(n)
		
		if t != 'intron': continue
		
		introns.append( (c, b, e, n, s) )


# initialize pwm
don = []
for i in range(6):
	don.append({'A':0, 'C':0, 'G':0, 'T':0})

acc = []
for i in range(8):
	acc.append({'A':0, 'C':0, 'G':0, 'T':0})

# get all sequences of splice site
for c, b, e, n, s in introns:
	if s == '+':
		iseq = chrom[c][b:e+1]
	else:
		iseq = mcb185.anti_seq(chrom[c][b:e+1])
		
	dseq = iseq[0:6]
	for i, nt in enumerate(dseq):
		don[i][nt] += 1
			
	aseq = iseq[-8:]
	for i, nt in enumerate(aseq):
		acc[i][nt] += 1


# print pwm
print_pwm(acc, 'ma001', 'ACC', 'splice acceptor')
print_pwm(don, 'ma002', 'DON', 'splice donor')
