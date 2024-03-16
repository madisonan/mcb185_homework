"""
import sys

print(sys.argv)

print(sys.argv[1][2])


matrix = [
	[1, 2, 3,],
	[4, 5, 6,],
	[7, 8, 9],
]

print(matrix)
print(matrix[2][0])
"""
"""
import json

person = {
	'name': 'Madi An',
	'age': 21,
	'weight': 17,
	'married': False,
	'pets': ['Tucker', 'Silvy', 'Snoopy'],
	'mentors': {
		'Dr. Begun': 'princicipal investigator',
		'Libby': 'lab manager',
	}
}

print(json.dumps(person, indent=4))

people = []
people.append(person)
people[0]['made this up'] = 'hello'
people[0]['mentors']['Rachel'] = 'postdoc'
people[0]['pets'].append('Goose')

print(json.dumps(people, indent = 4))
#print(people[0]['mentors']['Dr. Begun'])
"""
"""
import sys
import json
import mcb185

k = int(sys.argv[2])
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in rainge(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 1
		else: 				   kcount[kmer] += 1
print(kcount)

import sys
import json
import mcb185

k = int(sys.argv[2])
kloc = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	chrom = words[0]
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kloc: kloc[kmer] = {}
		if chrom not in kloc[kmer]: kloc[kmer][chrom] = []
		kloc[kmer][chrom].append((i))

print(json.dumps(kloc, indent = 4))


# for 83: get all of sequence in sequence variable so can pull things out
# for 85: find cords in gff file from splice sites

"""
oligo = {
	'Name': 'S0116',
	'Length': 18,
	'Sequence': 'ATTAGGTGACACTATAG',
	'Description': 'SP6 promoter sequencing primer'}
catalog = []
catalog.append(oligo)

def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name': name,
				'Length': length,
				'Sequence': seq,
				'Description': desc
			}
			catalog.append(record)
	return catalog

catalog = read_catalog('primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])
