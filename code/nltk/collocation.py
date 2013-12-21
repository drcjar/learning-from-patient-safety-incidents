import nltk
from sys import argv
from nltk.collocations import *

script, inputfilename, threshold = argv
threshold = int(threshold)
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

bifinder = BigramCollocationFinder.from_words(nltk.corpus.genesis.words("%s" % inputfilename))

trifinder = TrigramCollocationFinder.from_words(nltk.corpus.genesis.words("%s" % inputfilename))

bifinder.apply_freq_filter(threshold)
trifinder.apply_freq_filter(threshold)

print "Top 10 bigrams with bigrams occuring less than three times filtered:"
print bifinder.nbest(bigram_measures.pmi, 10)

print "Top 10 trigrams with trigrams occuring less than three times filtered:"

print trifinder.nbest(trigram_measures.pmi, 10)



