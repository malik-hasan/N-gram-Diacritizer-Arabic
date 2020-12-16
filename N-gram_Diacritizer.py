#import sys
#sys.path.append(r'c:\users\c1994\anaconda3\lib\site-packages')
from pyarabic.araby import strip_tashkeel
from pyarabic.araby import strip_lastharaka



#PART 1: train the model

with open('L165_diacritized_corpus.txt',encoding='utf8') as document:
	lines = document.readlines()	

def ngram(n):
	"""Creates a n-gram dictionary of order n
	Structured as nested dictionaries
	{undiacritized n-grams : {diacritized n-grams : count} }"""
	#tokenize and pad
	sentences = [sentence.split() for sentence in lines if len(sentence.split()) > 0]
	for i in range(len(sentences)):
		sentences[i] = ['<s>' for _ in range(n - 1)] + sentences[i] + ['</s>']
	
	ngrams = {}
	for sent in sentences:
		for i in range(len(sent)):
			ngram = tuple([strip_lastharaka(word) for word in sent[i:i + n]])
			if len(ngram) < n:
				break
			undiacritized = tuple(strip_tashkeel(' '.join(ngram)).split())
			if undiacritized in ngrams:
				if ngram in ngrams[undiacritized]:
					ngrams[undiacritized][ngram] += 1
				else:
					ngrams[undiacritized][ngram] = 1
			else:
				ngrams[undiacritized] = {ngram : 1}
	return ngrams

#Create four levels of n-grams
gram1, gram2, gram3, gram4 = ngram(1), ngram(2), ngram(3), ngram(4)
ngram_models = (gram4, gram3, gram2, gram1)

#PART 2: test the model

def diacritize(input_text):
	"""Diacritizes the input text"""
	#tokenize and pad
	sentences = [sentence.split() for sentence in input_text if len(sentence.split()) > 0]
	for i in range(len(sentences)):
		sentences[i] = ['<s>' for _ in range(3)] + sentences[i] + ['</s>']
		
	output = []
	for sent in sentences:
		output_sent = []
		for i in range(len(sent)):
			diacritized = False
			undiacritized = tuple(sent[i:i + 4])
			if len(undiacritized) < 4:
				break
			for ngrams in ngram_models:#back off
				if undiacritized in ngrams:
					diacritized = max(ngrams[undiacritized], key=ngrams[undiacritized].get)
					break
			if not diacritized:#in case it's unable to diacritize, just leave the word plain
				diacritized = undiacritized
			output_sent.append(diacritized[-1])
			
		output.append(' '.join(output_sent[:-1]))
	return output

def evaluate(reference, output):
	accurate, total = 0, 0
	for ref_sent, out_sent in zip(reference, output):
		total += len(out_sent.split())
		for ref_word, out_word in zip(ref_sent.split(), out_sent.split()):
			if ref_word == out_word:
				accurate += 1
	return accurate / total
				
#1st test: diacritize sample from within training data
with open('L165_diacritized_sample.txt') as inputfile: #diacritized reference file
	reference = inputfile.readlines()
	
with open('L165_undiacritized_sample.txt') as inputfile: #undiacritized input file
	input_text = inputfile.readlines()
	
reference = [' '.join([strip_lastharaka(word) for word in line.split()]) for line in reference]
output = diacritize(input_text)

print('accuracy from corpus sample: {0:.2f}%'.format(evaluate(reference, output) * 100))

#2nd test: diacritize testing data from outside the training data
with open('L165_diacritized_test.txt') as inputfile: #diacritized reference file
	reference = inputfile.readlines()
	
with open('L165_undiacritized_test.txt') as inputfile: #undiacritized input file
	input_text = inputfile.readlines()
	
reference = [' '.join([strip_lastharaka(word) for word in line.split()]) for line in reference]
output = diacritize(input_text)

print('accuracy from separate test data: {0:.2f}%'.format(evaluate(reference, output) * 100))
