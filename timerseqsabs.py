#File timeseqs.py

import sys,mytimer
reps=10000
repslist=range(reps)

def forLoop():
    res=[]
    for x in repslist:
        res.append(abs(x));
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs,repslist))

def genExpr():
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

print(sys.version)
for test in (forLoop,listComp,mapCall,genExpr,genExpr,genFunc):
    elasped,result=mytimer.timer(test)
    print('-'*30)
    print('%-9s: %.5f => [%s...%s]' %(test.__name__,elasped,result[0],result[-1]))


