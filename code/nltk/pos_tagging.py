import nltk

raw = open('computers.csv').read()

tokens = nltk.wordpunct_tokenize(raw)

text = nltk.Text(tokens)

words = [w.lower() for w in text]

tagged_text = nltk.pos_tag(text)

tag_fd = nltk.FreqDist(tag for (word, tag) in tagged_text)
