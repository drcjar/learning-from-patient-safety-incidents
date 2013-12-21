import nltk
from sys import argv

script, inputfilename, expression = argv

raw = open('%s' % inputfilename).read()

tokens = nltk.wordpunct_tokenize(raw)

text = nltk.Text(tokens)

text.concordance('%s' % expression, width=40, lines=100)

text.findall('<%s><to><.*><.*>' % expression)

words = [w.lower() for w in text]

c = nltk.ConcordanceIndex(text.tokens)

unableset = [text.tokens[offset+2] for offset in c.offsets('%s' % expression)]

print len(unableset)

words = [w.lower() for w in unableset]

vocab = sorted(set(words))

print len(vocab)

fdist = nltk.FreqDist(unableset)

fdist.plot(50, cumulative=True)

print vocab

