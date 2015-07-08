# Takes a newline delimited list of vocabulary words and outputs definitions ...
# to a CSV file.
# Args: Source txt file of newline-delimited words, Blank destination CSV file
#
# Requires nltk package installed according to these instructions:
# http://www.velvetcache.org/2010/03/01/looking-up-words-in-a-dictionary-using-python
# (Must run nltk.download() in Python interpreter and download wordnet.)

import csv
import sys
from nltk.corpus import wordnet

#fSource = open(sys.argv[1],'r')
#fDest = open(sys.argv[2],'w')
fSource = open('words.txt','r')
fDest = open('wordsDef.csv','w')

# words should be separated by newlines
words = fSource.read().splitlines()
print words

writer = csv.writer(fDest)

for word in words:
	# set of synonyms of word
	synset = wordnet.synsets(word)
	wordDef = ''

	# try to get the real definition
	try:
		# find first element of synset that is actually the word
		wordObj = next(x for x in synset if word in x.name())
		wordDef = wordObj.definition()

	# if the real def isn't in wordnet, define a synonym if possible
	except StopIteration:
		if not synset:
			pass
		else:
			syn = synset[0].name().split('.')[0]
			synDef = synset[0].definition()
			wordDef = 'appx. ' + syn + ' -- ' + synDef
	finally:
		print word + ":",
		print wordDef if wordDef else 'NO DEF. FOUND'

		# write to csv only if definition has been found
		if wordDef:
			writer.writerow( (word,wordDef) )

fSource.close()
fDest.close()