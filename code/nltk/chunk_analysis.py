import nltk 

raw = open('npchunks.txt').read() #loads incident descriptions identified as being due to computer problems

tokens = nltk.wordpunct_tokenize(raw) #tokenizes free text

# tokens = [nltk.PorterStemmer().stem(t) for t in tokens] 
# uncomment to stem tokens

#tokens = [nltk.WordNetLemmatizer().lemmatize(t) for t in tokens]
# uncomment to lemmatize tokens

text = nltk.Text(tokens) #defines text

words = [w.lower() for w in text] #defines words and makes all words lower case

vocab = sorted(set(words)) #defines vocabulary

print vocab[:100]

def lexical_diversity(text): #calculate lexical diversity
    return len(text) / len(set(words))

print "the number of words in the text is %d" % len(text)

print "the number of words in the vocabulary is %d" % len(vocab) 

print "lexical diversity is %d" % lexical_diversity(text) #prints lexical diversity

text.collocations() #builds collocations

fdist = nltk.FreqDist(text)

fdist.plot(50, cumulative=False) #prints a cumulative frequency distribution of the 50 most commonly used words in the text

text.dispersion_plot(["computer", "system", "crash", "bleep", "patient"]) #example dispersion plot using arbitary seach terms
