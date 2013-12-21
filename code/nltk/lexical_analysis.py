import nltk
from nltk.corpus import stopwords
from sys import argv

script, inputfilename = argv #takes whatever filename you pass in

print inputfilename

raw = open("%s" % inputfilename).read() #loads incident descriptions identified as being due to computer problems

tokens = nltk.wordpunct_tokenize(raw) #tokenizes free text

#tokens = [nltk.PorterStemmer().stem(t) for t in tokens] 
# uncomment to stem tokens

#tokens = [nltk.WordNetLemmatizer().lemmatize(t) for t in tokens]
# uncomment to lemmatize tokens

text = nltk.Text(tokens) #defines text

words = [w.lower() for w in text] #defines words and makes all words lower case

filtered_words = [w for w in words if w not in stopwords.words('english')] #removes commonly occuring words ("stop words")

vocab = sorted(set(words)) #defines vocabulary

def lexical_diversity(text): #calculate lexical diversity
    return len(text) / len(set(words))

print "the number of words in the text is %d" % len(text)

print "the number of words in the vocabulary is %d" % len(vocab) 

print "lexical diversity is %d" % lexical_diversity(text) #prints lexical diversity

text.collocations() #builds collocations

fdist = nltk.FreqDist(ch.lower() for ch in filtered_words if ch.isalpha())

fdist.plot(50, cumulative=True) #prints a cumulative frequency distribution of the 50 most commonly used words in the text

text.dispersion_plot(["computer", "system", "crash", "bleep", "patient"]) #example dispersion plot using arbitary seach terms
