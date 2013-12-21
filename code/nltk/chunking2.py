import pickle
import nltk
import nltk.tag
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize

raw = open('computers.csv').read()

sentences = sent_tokenize(raw)

wordsenttoke = [word_tokenize(t) for t in sent_tokenize(raw)]

#chunks = nltk.tag.batch_pos_tag(wordsenttoke)

pkfl = open('chunks.pkl', 'rb')
chunks = pickle.load(pkfl)


patterns = """
NP:  {<DT|PP\$>?<JJ>*<NN>}

"""


NPChunker = nltk.RegexpParser(patterns)

result = NPChunker.parse(chunks[1])

print result

result.draw()

#how to save with pickle
#>>> import pickle
#>>> vocab =["cheese", "spam", "eggs"]
#>>> outf=open('vocab.pkl','wb')
#>>> pickle.dump(vocab,outf)
#>>> outf.close()
#>>> quit()
