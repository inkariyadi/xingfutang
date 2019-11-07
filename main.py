import kode
import vektor 
from scipy.misc.pilutil import imread
import matplotlib.pyplot as plt

#je : euclidean
#cs : cosin
vector = []
fileimg = []

folder = "dataset/"
print("masukkan file name")
filename=str(input(""))

print("masukkan metod")
metode=str(input(""))
vector = kode.loadVector() #mindahin ke array 
fileimg = kode.loadNamaFile() #mindahin ke array

vInit = kode.extract_features(filename) #hasil vektor yg mau di compare

hasilje = [0 for i in range(len(vector))] #nyimpen hasil jarak euclidean
hasilcs = [0 for i in range(len(vector))] #nyimpen hasil cosin

hasil = ["" for i in range(10)]
if(metode=="je"):
    for i in range (len(vector)):
        hasilje[i] = vektor.euclidean(vInit,vector[i])

    for i in range (10):
        maks = vektor.haslowest(hasilje)
        hasilje[maks]=1000
        hasil[i]=fileimg[maks]
        img = imread(folder+hasil[i], mode="RGB")
        plt.imshow(img)
        plt.show()
else:
    for i in range (len(vector)):
        hasilje[i] = vektor.cosine(vInit,vector[i])

    for i in range (10):
        maks = vektor.hashighest(hasilje)
        hasilje[maks]=-1000
        hasil[i]=fileimg[maks]
        img = imread(folder+hasil[i], mode="RGB")
        plt.imshow(img)
        plt.show()


