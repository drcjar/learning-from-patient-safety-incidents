import nltk
import pickle

from nltk.chunk import ne_chunk

pkfl = open('ne_chunks.pkl', 'rb')

ne_chunks = pickle.load(pkfl)

#need to work out how to analyse noun phrase list
#need to apply NER to POS tagged sentances and extract relations (without firstchunking to noun phrases)

def sub_leaves(tree, node):
    return [t.leaves() for t in tree.subtrees
    (lambda s: s.node == node)]

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


