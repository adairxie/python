
def mymap(func,*seqs):
    res=[]
    for args in zip(*seqs):
        res.append(func(*args))
    return res

print(mymap(abs,[-2,-1,0,1,2,3]))
print(mymap(pow,[1,2,3],[2,3,4,5]))
