import nltk
import pickle

pkfl = open('chunks.pkl', 'rb')

chunks = pickle.load(pkfl)

patterns =  "NP:{<DT>?<JJ>*<NN>}"

NPChunker = nltk.RegexpParser(patterns)

nplist = []

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

outf = open('ne_chunks.pkl', 'wb')
pickle.dump(ne_chunks, outf)
outf.close()

#pkfl = open('ne_chunks.pkl', 'rb')
#ne_chunks = pickle.load(pkfl)

print ne_chunks

ne_chunks[7].draw()

#fdist = nltk.FreqDist(nplist)
#fdist.plot(50, cumulative=True)

