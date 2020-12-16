# Accuracy test using Word Error Rate
""" The following code uses minimal distance between two strings. It was the code inspired by Martin Thomas's website, the document totled "Wor Error Rate Calculation". The link can be found at the works cited page of the final proposal."""

import numpy

def wer(r, h):	# returns a integer for the error score
	d = numpy.zeros((len(r) + 1) * (len(h) + 1), dtype=numpy.uint8)	# creating an array
	d = d.reshape((len(r) + 1, len(h) + 1))
	for i in range(len(r) + 1):
		for j in range(len(h) + 1):
			if i == 0:
				d[0][j] = j
			elif j == 0:
				d[i][0] = i	# array of 0 to len(r), len(h), and zeros in the middle


	for i in range(1, len(r) + 1):	# counts the number of changes
		for j in range(1, len(h) + 1):
			if r[i - 1] == h[j - 1]:
				d[i][j] = d[i - 1][j - 1]	# when the compared elements are the same
			else:			# when not the same
				substitution = d[i - 1][j - 1] + 1
				insertion = d[i][j - 1] + 1
				deletion = d[i - 1][j] + 1
				d[i][j] = min(substitution, insertion, deletion)	# get the smallest number

	return d[len(r)][len(h)]	# the "last" index position of 2-D array 

# Main:
# Opening the test file of undiacritized Arabics and use the function to add diarcitics.
with open('L165_undiacritized_test.txt',encoding='utf8') as inputfile: #input file
	input_text = inputfile.readlines()
s=diacritize(input_text)

# Opening the test file of diacritized Arabics to make comparison.
s2=''
f=open('L165_diacritized_test.txt',encoding='utf8')
for line in f:
        lines=line.strip()
        s2 += ''.join(lines[:-1]) +'.'
       
error=wer(s,s2)
acc=(len(s2)-error)/len(s2)
print(acc)

