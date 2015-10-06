#传入一个任意的比较函数，实现通用化单个的函数计算无论最小值还是最大值。
def minmax(test, *args):
    res=args[0]
    for arg in args[1:]:
        if test(arg, res):
            res=arg
    return res
    
def lessthan(x,y): return x < y #see also lambda
def grtrthan(x,y): return x > y 

print(minmax(lessthan,4,2,1,5,6,3)) #self-test code
print(minmax(grtrthan,4,2,1,5,6,3))



%python minmax.py
1
6
