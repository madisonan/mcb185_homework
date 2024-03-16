# authors: Madison An and Jaime Young

import json
import gzip
import sys

filepath = sys.argv[1]
records = []
with gzip.open(filepath, 'rt') as fp:
	uid = ''
	for line in fp:
		if line.startswith('ID'):
			uid = line.split()[1]
		elif line.startswith('PO'):
			pwm = []
			for line in fp:
				if line.startswith('XX'): 
					records.append({'id': uid, 'pwm': pwm})
					break
				name, a, c, g, t = line.rstrip().split('\t')
				counts = {
					'A': a,
					'C': c,
					'G': g,
					'T': t
				}
				pwm.append(counts)
print(json.dumps(records, indent=4))