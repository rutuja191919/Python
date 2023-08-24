import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TKAgg')
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

print("-----Marvellous Infosystems-------")

print("----Dibetes prdictor using Decision Tree----")

dibetes = pd.read_csv('diabetes.csv')

print("Columns of Dataset")
print(dibetes.columns)

print("First 5 records of dataset")
print(dibetes.head())

print("Dimension of dibetes data : {}".format(dibetes.shape))

X_train, X_test, Y_train, Y_test = train_test_split(dibetes.loc[:,dibetes.columns != 'Outcome'], dibetes['Outcome'], stratify = dibetes['Outcome'], random_state = 66)

tree = DecisionTreeClassifier(random_state=0)
tree.fit(X_train, Y_train)

print("Accuracy on training set : {:.3f}".format(tree.score(X_train, Y_train)))
print("Accuracy on test set : {:.3f}".format(tree.score(X_test, Y_test)))

tree1 = DecisionTreeClassifier(max_depth=3, random_state=0)
tree1.fit(X_train, Y_train)

print("Accuracy on training set : {:.3f}".format(tree1.score(X_train, Y_train)))
print("Accuracy on test set : {:.3f}".format(tree1.score(X_test, Y_test)))

print("Feature Importance : \n{}".format(tree.feature_importances_))

def plot_feature_importances_diabetes(model):
    plt.figure(figsize = (8,6))
    n_features = 8
    plt.barh(range(n_features), model.feature_importances_, align = 'center')
    diabetes_features = [x for i, x in enumerate(dibetes.columns) if i!= 8]
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.ylim(-1, n_features)
    plt.show()

plot_feature_importances_diabetes(tree)