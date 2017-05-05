import random

def bubbleSort(l):
    lngth = len(l)
    while(lngth):
        for idx in range(lngth):
            if idx < lngth-1:
                x = l[idx]
                y = l[idx+1]
                if x > y:
                    l[idx] = y
                    l[idx+1] = x
        lngth-=1
    return l


p = [7,4,1,8,5,6,3,2]
q = [9,39,17,3,78]
r = [1000,9,42,854,99]
print bubbleSort(p)
print bubbleSort(q)
print bubbleSort(r)
s = []
for i in range(1,101):
    s.append(int(10000*random.random()))
print s
print bubbleSort(s)
