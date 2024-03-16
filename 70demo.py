import random



"""
# dictionary for hydropathy of each aa
# dictionary is made with curly brackets; has pair values
# if use a global variable, capitalize it 
KDT = {'I':4.5, 'V':4.2, 'L':3.8, 'F':2.8, 'C':2.5, 'M':1.9, 'A':1.8,
    'G':-0.4, 'T':-0.7, 'S':-0.8, 'W':-0.9, 'Y':-1.3, 'P':-1.6, 'H':-3.2,
    'E':-3.5, 'Q':-3.5, 'D':-3.5, 'N':-3.5, 'K':-3.9, 'R':-4.5}

def kd_dict(seq):
	kdsum = 0
	for aa in seq: 
		if aa in KDT: kdsum += KDT[aa]
	return kdsum / len(seq)


# make a random protein
protein_length = 300
protein = []
for i in range(protein_length):
	aa = random.choice('ACDEFGHIKLMNPQRSTVWY')
	protein.append(aa)
protein = ''.join(protein)

for i in range(1000):
	sumh = 0
	for aa in protein:
		sumh += kd_dict(aa)


size = 10000
words = []
for i in range(size):
	token = []
	for j in range(10):
		token.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	token = ''.join(token)
	words.append(token)

for i in range(1000):
	if 'MYNAMEMADI' in words:
		print('found')

for aas in itertools.product('ACDEFGHIKLMNPQRSTVWY')
	# ^ this is not done idk what was here

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kcount: kcount[kmer] = 0
	kcount[kmer] += 1

for kmer, n in kcount.items():
	print(kmer, n)
"""