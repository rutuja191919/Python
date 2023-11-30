import numpy as np
import pandas as pd
from copy import deepcopy
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt

def MarvellousKMean():
    print("________________")
    #Set three centers the model should predict similar results
    center_1 = np.array([1,1])
    print(center_1)
    print("________________")
    center_2 = np.array([5,5])
    print(center_2)
    print("_________________")
    center_3 = np.array([8,1])
    print(center_3)
    print("_________________")

    #Generate random data and center it to three centers
    data_1 = np.random.randn(7,2) + center_1
    print("Elements of first cluster with size"+str(len(data_1)))
    print(data_1)
    print("_________________")
    data_2 = np.random.randn(7,2) + center_2
    print("Elements of second cluster with size"+str(len(data_2)))
    print(data_2)
    print("_________________")
    data_3 = np.random.randn(7,2) + center_3
    print("Elements of third cluster with size"+str(len(data_3)))
    print(data_3)
    print("_________________")
    data = np.concatenate((data_1, data_2, data_3), axis = 0)
    print("size of complete data set"+str(len(data)))
    print(data)
    print("_________________")
    plt.scatter(data[:,0],data[:,1], s = 7)
    plt.title("Marvellous Infosystems : Input Dataset")
    plt.show()
    print("__________________")


    #Number of clusters
    k = 3

    #Number of training data
    n = data.shape[0]
    print("Total number of elements are",n)
    print("-----------------")

    #No of features in the data
    c = data.shape[1]
    print("Total number of features are",c)
    print("_________________")

    #Generate random centers, here we use sigma and mean to ensure it to represent the whole data
    mean = np.mean(data, axis = 0)
    print("Value of mean", mean)
    print("_________________")

    #Calculate the standard deviation
    std = np.std(data, axis = 0)
    print("Value of std",std)
    print("__________________")

    centers = np.random.randn(k,c)*std + mean
    print("Random centers are : ",centers)
    print("__________________")

    #Plot the data and centers generated as random
    plt.scatter(data[:,0], data[:,1], c='r', s=7)
    plt.scatter(centers[:,0], centers[:,1], marker = "*", c= 'g', s = 150)
    plt.title("Marvellous Infosystems : Input dataset with random centroid *")
    plt.show()
    print("__________________")

    centers_old = np.zeros(centers.shape)    #to store old centers
    centers_new = deepcopy(centers)

    print("Value of old centroids")
    print(centers_old)
    print("____________________")

    print("Value of new centroids")
    print(centers_new)
    print("____________________")

    data.shape
    clusters = np.zeros(n)
    distances = np.zeros((n,k))

    print("Initial distances are")
    print(distances)
    print("____________________")

    error = np.linalg.norm(centers_new - centers_old)
    print("Value of error is ",error)

    #When, after af update, the estimate of that center stays the same, exit loop
    while error != 0:
        print("Value of error is : ",error)
        #Measure the distance to every center
        print("Measure the distance to every center")
        for i in range(k):
            print("Iteration number",i)
            distances[:,i] = np.linalg.norm(data - centers[i], axis = 1)

        #Assign all training data to closest center
        clusters = np.argmin(distances, axis = 1)

        centers_old = deepcopy(centers_new)

        #Calculate mean for every cluster and update the center
        for i in range(k):
            centers_new[i] = np.mean(data[clusters == i], axis = 0)
        error = np.linalg.norm(centers_new - centers_old)
        print("Value of error is : ", error)
        #End of while
    centers_new

    #Plot the data and centers generated as random
    plt.scatter(data[:,0],data[:,1], s = 7)
    plt.scatter(centers_new[:,0], centers_new[:,1], marker = "*", c = 'g', s= 150)
    plt.title("Marvellous Infosystems : Final data with Centroids")
    plt.show()

def main():
    print("_________Marvellous Infosystems_____________")
    print("Unsupervised Machine Learning")
    print("Clustering using K Mean algorithm")

    MarvellousKMean()

if __name__ == "__main__":
    main()