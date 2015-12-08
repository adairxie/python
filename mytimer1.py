# File mytimer.py

import time
reps= 1000
repslist=range(reps)

def timer(func, *pargs,**kargs):
    start=time.clock()
    for i in repslist:
        ret=func(*pargs,**kargs)
    clapsed=time.clock() -start
    return (clapsed,ret)
