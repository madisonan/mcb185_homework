# authors: Madison An and Jaime Young

# genome stats

import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]
genome_type = sys.argv[3]

if feature == 'counts':
	g_count = 0
	with gzip.open(gffpath, 'rt') as gc:
		for line in gc:
			words = line.split()
			if words[2] == genome_type:
				g_count += 1
	print(g_count)

#min
def minimum(y):
	mini = distances[0]
	for val in distances:
		if val < mini: mini = val
	return mini
	
if feature == 'minimum':
	distances = []
	with gzip.open(gffpath, 'rt') as mi:
		for line in mi:
			words = line.split()
			if words[2] == genome_type:
				distance = int(words[4]) - int(words[3]) + 1
				distances.append(distance)
		print(minimum(distances))

#max
def maximum(y):
	maxi = y[0]
	for val in y:
		if val > maxi: maxi = val
	return maxi
	
if feature == 'maximum':
	distances = []
	with gzip.open(gffpath, 'rt') as ma:
		for line in ma:
			words = line.split()
			if words[2] == genome_type:
				distance = int(words[4]) - int(words[3]) + 1
				distances.append(distance)
		print(maximum(distances))
		
		
#mean
def mean(y):
	total = 0
	for distance in distances:
		total += distance
	return total / len(distances)
	
if feature == 'mean':
	distances = []
	with gzip.open(gffpath, 'rt') as me:
		for line in me:
			words = line.split()
			if words[2] == genome_type:
				distance = int(words[4]) - int(words[3]) + 1
				distances.append(distance)
		print(round(mean(distances)))
				

#SD
def stdev(y):
	total = 0
	means = 0
	for distance in distances:  
		total += distance                 
	mean = total / len(distances)
	for distance in distances:
		sums = (distance - mean) ** 2
		means += sums
	return math.sqrt(means / len(distances) - 1)
	
if feature == 'stdev':
	distances = []
	with gzip.open(gffpath, 'rt') as sd:
		for line in sd:
			words = line.split()
			if words[2] == genome_type:
				distance = int(words[4]) - int(words[3]) + 1
				distances.append(distance)
		print(round(stdev(distances)))


#median
def median(y):
	distances.sort()
	if len(distances) % 2 == 0:
		med = (distances[len(distances) // 2] + distances[(len(distances) // 2) - 1]) / 2
	else:
		med = distances[len(distances) // 2]
	return med


if feature == 'median':
	distances = []
	with gzip.open(gffpath, 'rt') as sd:
		for line in sd:
			words = line.split()
			if words[2] == genome_type:
				distance = int(words[4]) - int(words[3]) + 1
				distances.append(distance)
		print(round(median(distances)))
