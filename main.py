import kode
import vektor 
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

hasilje = [] #nyimpen hasil jarak euclidean
hasilcs = [] #nyimpen hasil cosin
for i in range (len(vector)):
    hasilje[i] = vektor.euclidean(vInit[i],vector[i],2048)
    hasilcs[i] = vektor.cosine(vInit[i],vector[i],2048)

hasilje.sort() #sort menaik
hasilcs.sort(reverse=True) #sort menurun
sortfileje = [x for _,x in sorted(zip(hasilje,fileimg))]
sortfilecs = [x for _,x in sorted(zip(hasilcs,fileimg))]

hasil = []
if(metode=="je"):
    for i in range (10):
        hasil[i]=sortfileje[i]
        img = imread(hasil[i], mode="RGB")
        plt.imshow(img)
        plt.show()
else:
    for i in range (10):
        hasil[i]=sortfilecs[i]
        img = imread(hasil[i], mode="RGB")
        plt.imshow(img)
        plt.show()

