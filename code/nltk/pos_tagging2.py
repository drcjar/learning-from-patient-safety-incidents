from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize

from nltk.tag import pos_tag

raw = open('computers.csv').read()

sentences = sent_tokenize(raw)

tagged = pos_tag(word_tokenize(sentence[1]))

entities = nltk.chunk.ne_chunk(tagged)

entities.draw()

wordsenttoke = [word_tokenize(t) for t in sent_tokenize(raw)]

chunks = nltk.tag.batch_pos_tag(sentences)

