import cv2
import numpy as np
import scipy
from scipy.misc import imread
import pickle as pickle
import random
import os
import matplotlib.pyplot as plt

# Feature extractor
def extract_features(image_path, vector_size=32):
    image = imread(image_path, mode="RGB")
    print("Extracting ficurs from" +image_path)
    try:
        alg = cv2.KAZE_create()
        # Dinding image keypoints
        kps = alg.detect(image)
        # Getting first 32 of them. 
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(image, kps)
        # Flatten all of them in one big vector - our feature vector
        dsc = dsc.flatten()
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            # if we have less than 32 descriptors then just adding zeros at the 
            # end of our feature vector
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print ('Error: '), e
        return None

    return dsc

#prosedur untuk menyimpan vektor ke vector.pck
def saveVector(): 
    data = os.listdir("dataset/")
    vec = [0 for i in range (len(data))] #berisi data vector 
    for i in range (len(data)):
        vec[i]=extract_features("dataset/"+data[i])
    with open('vector.pck', 'wb') as fopen:
        pickle.dump(vec, fopen)
    fopen.close()

#prosedur untuk menyimpan nama-nama file ke nama_file.pck
def saveNamaFile(): 
    data = os.listdir("dataset/")
    namafile = [0 for i in range (len(data))] #berisi nama file 
    for i in range (len(data)):
        namafile[i]=data[i]
    with open('nama_file.pck', 'wb') as fopen:
        pickle.dump(namafile, fopen)
    fopen.close()


#fungsi yang mengembalikan array of vector
def loadVector(): 
    fopen= open('vector.pck','rb')
    fload= pickle.load(fopen) #array of vector
    fopen.close()
    vector=[0 for i in range (len(fload))]
    for i in range (len(fload)):
        vector[i]=fload[i]
    return vector

#fungsi yang mengembalikan array of nama file
def loadNamaFile(): 
    fopen= open('nama_file.pck','rb')
    fload= pickle.load(fopen) #array of namafile
    fopen.close()
    namafile=["" for i in range (len(fload))]
    for i in range (len(fload)):
        namafile[i]=fload[i]
    return namafile





