import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TKAgg')
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

print("----Marvellous Infosystems----")

print("---Diabetes predictor using Random Forest----")

diabetes = pd.read_csv('diabetes.csv')

print("Columns of dataset")
print(diabetes.columns)

print("First 5 records of dataset")
print(diabetes.head())

print("Dimension of diabetes data : {}".format(diabetes.shape))

X_train, X_test, Y_train, Y_test = train_test_split(diabetes.loc[:, diabetes.columns != 'Outcome'], diabetes['Outcome'], stratify=diabetes['Outcome'], random_state = 66)

training_accuracy = []
test_accuracy = []

#try n_neighbors from 1 to 10
neighbors_setings = range(1,11)

for n_neighbors in neighbors_setings:
    #build the model
    knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train, Y_train)
    #record training set accuracy
    training_accuracy.append(knn.score(X_train, Y_train))
    #record test set accuracy
    test_accuracy.append(knn.score(X_test, Y_test))

plt.plot(neighbors_setings,training_accuracy,label = "Training accuracy")
plt.plot(neighbors_setings,test_accuracy, label = "Test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.savefig('knn_compare_model')
plt.show()

knn = KNeighborsClassifier(n_neighbors = 9)

knn.fit(X_train, Y_train)

print("training set accuracy : {:.2f}".format(knn.score(X_train, Y_train)))
print("test set accuracy : {:.2f}".format(knn.score(X_test, Y_test)))


