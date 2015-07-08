# Interactive program that gets word definitions.
#
# Takes a newline delimited list of vocabulary words and outputs definitions ...
# to a CSV file. USER PICKS THE DEFINITIONS.
# Args: Source txt file of newline-delimited words, Blank destination CSV file
#
# Requires nltk package installed according to these instructions:
# http://www.velvetcache.org/2010/03/01/looking-up-words-in-a-dictionary-using-python
# (Must run nltk.download() in Python interpreter and download wordnet.)

import csv
import sys
from nltk.corpus import wordnet

def candidateDefs(word):
	synset = wordnet.synsets(word)
	wordObjs = [x for x in synset if word + '.' in x.name()]

	if wordObjs:
		return wordObjs
	else:
		return synset

def defineWord(word):
	# get the definition candidates
	candidates = candidateDefs(word)

	if not candidates:
		return ''
	if len(candidates) == 1:
		return candidates[0].definition()

	# pritn the definition options
	for n, wordObj in enumerate(candidates):
		appx = '' if word + '.' in wordObj.name() else 'appx. '
		print '%d %s%s: %s' % (n, appx, wordObj.name().split('.')[0], wordObj.definition())
	
	print 'Choose definition for \"%s\" by entering the number next to it.' % word

	while True:
		s = raw_input('--> ')
		try:
			chosenIndex = int(s)
			if chosenIndex in range(len(candidates)):
				break
			else:
				print 'Number out of range.'
				continue
		except ValueError:
			print 'Must enter a number.'
			continue

	appx2 = '' if word + '.' in candidates[chosenIndex].name() else 'appx. '
	return '%s%s' % (appx2, candidates[chosenIndex].definition())

#fSource = open(sys.argv[1],'r')
#fDest = open(sys.argv[2],'w')
fSource = open('words.txt','r')
fDest = open('wordsDef.csv','w')

# words should be separated by newlines
words = fSource.read().splitlines()
print words

writer = csv.writer(fDest)

for word in words:
	wordDef = defineWord(word)
	if wordDef:
		writer.writerow( (word,wordDef) )
	#print word, wordDef

fSource.close()
fDest.close()
