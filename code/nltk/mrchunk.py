import nltk
import nltk.tag
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from sys import argv


script, inputfilename = argv

raw = open("%s" % inputfilename).read()

sentences = sent_tokenize(raw)

wordsenttoke = [word_tokenize(t) for t in sent_tokenize(raw)]

chunks = nltk.tag.batch_pos_tag(wordsenttoke)

patterns =  "NP:{<DT>?<JJ>*<NN>}"

NPChunker = nltk.RegexpParser(patterns)

nplist = []

def sub_leaves(tree, node):
    return [t.leaves() for t in tree.subtrees
    (lambda s: s.node == node)]

def chunk(patterns):
    for sent in chunks:
        tree = NPChunker.parse(sent)
        for subtree in tree.subtrees():
            if subtree.node == 'NP':
                print subtree
                nplist.append(subtree)
chunk(patterns)

print len(nplist)

ne_chunks = nltk.batch_ne_chunk(nplist) 

print ne_chunks

for i in range(len(ne_chunks)):
    tree = ne_chunks[i]
    print 'PERSON'
    print sub_leaves(tree, 'PERSON')


for i in range(len(ne_chunks)):
     tree = ne_chunks[i]
     print 'ORGANIZATION' 
     print sub_leaves(tree, 'ORGANIZATION')

for i in range(len(ne_chunks)):
     tree = ne_chunks[i]
     print 'GPE' 
     print sub_leaves(tree, 'GPE')

#fdist = nltk.FreqDist(nplist)
#fdist.plot(50, cumulative=True)

