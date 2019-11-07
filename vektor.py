import math

def euclidean(x,y):
    sum = 0
    for i in range(len(y)):
        sum += math.pow((x[i]-y[i]),2)
    return math.sqrt(sum)

def dotproduct(x,y):
    dot = 0
    for i in range(len(x)):
        dot += x[i] * y[i]
    
    return dot

def norm(x):
    sum = 0
    for i in range(len(x)):
        sum += math.pow(x[i],2)    
    return math.sqrt(sum)

def cosine(x,y):
    return dotproduct(x,y) / (norm(x)*norm(y))

def haslowest(cek):
    minn=0
    for i in range (len(cek)):
        if(cek[i]<cek[minn]):
            minn=i
    return minn

def hashighest(cek):
    maks=0
    for i in range (len(cek)):
        if(cek[i]>cek[maks]):
            maks=i
    return maks
    
