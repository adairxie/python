#!/usr/bin/python 

def myzip(*seqs):
    seqs=[list(S) for S in seqs]
    while all(seqs):
      yield  tuple(S.pop(0) for S in seqs)

def mymapPad(*seqs,pad=None):
    seqs=[list(S) for S in seqs ]
    while any(seqs):
       yield tuple((S.pop(0) if S else pad) for S in seqs)

S1, S2='abc','xyz123'
print(list(myzip(S1,S2)))
print(list(mymapPad(S1,S2)))
print(list(mymapPad(S1,S2,pad=99)))
