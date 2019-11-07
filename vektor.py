import math

def euclidean(x,y,z):
    sum = 0
    for i in range(z):
        sum += math.pow((x[i]-y[i]),2)
    return math.sqrt(sum)

def dotproduct(x,y,z):
    dot = 0
    for i in range(z):
        dot += x[i] * y[i]
    
    return dot

def norm(x,z):
    sum = 0
    for i in range(z):
        sum += math.pow(x[i],2)    
    return math.sqrt(sum)

def cosine(x,y,z):
    return dotproduct(x,y,z) / (norm(x,z)*norm(y,z))

def haslowest(cek):
    minn=0
    for i in range (len(cek)):
        minn = cek[i]
        if(cek[i]<minn):
            minn=i
    return minn

def haslowest(cek):
    maks=0
    for i in range (len(cek)):
        maks = cek[i]
        if(cek[i]>maks):
            maks=i
    return maks
    
