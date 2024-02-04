#while loops

i = 0
while i < 3:
	print(i)
	i = i + 1
print('final value of i is', i)



#for loops

for i in range(1, 10, 3):
	print(i)
#1 is the initial value, 10 is the value to stop before, 3 is the increment

for i in range(0, 5):
	print(i)
#i will auto increment by 1 so don't need last input

for char in 'hello':
	print(char)
#printing every character in hello bc hello is a string

seq = 'GAATTC'
for nt in seq:
	print(nt)
#defined seq and then said for every nt in that print that nt out
#so it this is also printing out characters bc seq is a string


#nested loops

for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:		   print(nt1, nt2, '-1')
#why does this one list so many letters and why do they list differently
#goes four times because outer loop is compared to every value of inner loop
	#so a in nt1 compared to a and c and g and t in nt2

nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:		   print(nt1, nt2, '-1')

limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)
#second loop starts one after outer loop so it doesn't compare the same value to itself
#outer loop does 0, 1, 2, 3 and inner loop does, 1, 2, 3, 4

"""
#matrix patterns:
	for i in range(1, limit):
		for j in range(1, limit):
#half matrix including major diagonal:
	for i in range(1, limit):
		for j in range(i, limit):
#half matrix not including major diagonal:
	for i in range(1, limit):
		for j in range(i + 1, limit):
#full matrix not including major diagonal:
	for i in range(1, limit):
		for j in range(1, limit):
			if i != j:
				print()
"""