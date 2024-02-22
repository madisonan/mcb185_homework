# string container holds letters, first position is called 0
# so seq[0] refers to G
seq = 'GAATTC'
print(seq[0], seq[1])


# can iterate through letters by indices using range() and use len() to set limit
# len is like length of the string you go to
for i in range(len(seq)):
	print(i, seq[i])


# SLICES
# slices are subset of container
# slices work like range() taking initial position and end-before limit
# use colon instead of comma though
s = 'ABCDEFGHIJ'
print(s[0:5])	# 0 is initial position and 5 is the end before limit

# can also have a step size, the last value in [] is how much go up
print(s[0:8:2])	# goes up by 2 every time instead of just 1

# can omit initial val, which is replaced by 0, or final val, which is length of string
print(s[0:5], s[:5])		# both ABCDE
print(s[5:len(s)], s[5:])	# both FGHIJ
# s[0] is the same thing as s[0:1]
# s is same as s[0:len(s)] and s[::] and s[::1]
# s[::-1] spits out the string in reverse 
print(s, s[::], s[::1], s[::-1])


# TUPLES
# tuples hold multiple values. constructed with comma-separated
tax = ('Homo', 'sapiens', 9606)	# construct tuple
print(tax)						# note the parenthesis in output

# cannot change contents of tuples and strings once they are set
# s[0] = 'C'	# generates error
# tax			# generates error

# can slice tuples, though
print(tax[0])		# index
print(tax[::-1])	# slice

# quadratic function we made before returns a tuple
def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2
# can either unpack into separate variables or capture entire tuple in one variable
# always better to unpack tuple !!!
x1, x2 = quadratic(5, 6, 1)		# unpacked tuple - yes
print(x1, x2)						#pretty
intercepts = quadratic(5, 6, 1)	# packed tuple - no
print(intercepts[0], intercepts[1])	# ugly



# ENUMERATE()
# this one does the normal version
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])

# for i in range whatever makes it go through a defined amount of times
# enumerate will do it for you instead of having to do it yourself
# basically either has indices and vals separate 
# or in enumerate make tuple with both index and values in separate named variables

# this one provide tuple containing the index and val in separate named variables
for i, nt in enumerate(nts):
	print(i, nt)



# ZIP()
# can use range() to simultaneously index separate containers
# but problem is need the same number of things in nts and names or error 
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(nts)):
	print(nts[i], names[i])
# can use zip instead to just get an element from each container and return in a tuple
# will also just end when the shorter container runs out
for nt, name in zip(nts, names):
	print(nt, name)



# LISTS
# lists are like tuples but can change their contents
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'	#changing spot 2 (last one in this case) to G instead of C
print(nts)

# can add things to the end of lists with list.append()
nts.append('C')
print(nts)


# NOTES FOR HOMEWORK
# collect all the length for exon and then divide by number of exons = avg exon length














