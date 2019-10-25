import math

def jarak(x,y):
    sum = 0
    for i in range(1,3):
        sum += math.pow(x[i]-y[i],2)

    return math.sqrt(sum)

def dotproduct(x,y):
    dot = 0
    for i in range(1,3):
        dot += x[i] * y[i]
    
    return dot

def norm(x):
    sum = 0;

    for i in range(1,3):
        sum += math.pow(x[i],2)
    
    return math.sqrt(sum)

def cosine(x,y):
    return dotproduct(x,y) / norm(x) / norm(y)
    
x = [0,10,5]
y = [0,10,5]

print(jarak(x,y))
print(dotproduct(x,y))
print(norm(x))
print(norm(y))
print(cosine(x,y))