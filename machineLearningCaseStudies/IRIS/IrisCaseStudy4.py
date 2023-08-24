from sklearn import tree
from sklearn.datasets import load_iris
from scipy.spatial.distance import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

class MarvellousKNeighborsClassifier:
    def fit(self, trainingdata, trainingtarget):
        self.TrainingData = trainingdata
        self.TrainingTarget = trainingtarget

    def closest(self,row):
        minimumdistance = euclidean(row,self.TrainingData[0])
        minimumindex = 0

        for i in range(1,len(self.TrainingData)):
            Distance = euclidean(row,self.TrainingData[i])
            if Distance < minimumdistance:
                minimumdistance = Distance
                minimumindex = i

        return self.TrainingTarget[minimumindex]

    def predict(self, TestData):
        predictions = []
        for value in TestData:
            result = self.closest(value)
            predictions.append(result)

        return predictions

def MarvellousML():
    border = "-"*50

    Dataset = load_iris()

    Data = Dataset.data
    Target = Dataset.target

    print(border)
    print("Actual data set")
    print(border)

    for i in range(len(Dataset)):
        print("ID: %d,Feature %s, Label %s"%(i,Dataset.data[i],Dataset.target[i]))
        print("Size of actual data set %d"%(i+1))

    Data_train, Data_test, Target_train, Target_test = train_test_split(Data,Target,test_size = 0.5)    #shuffle the dataset as every label should be there in training of the data
    #testsize : kiti data konala training and testing la - 0.3 asel tar testing la 70% janar

    print(border)
    print("Training data set")
    print(border)
    for i in range(len(Data_train)):
        print("ID: %d,Feature %s, Label %s" % (i, Data_train[i], Target_train[i]))
        print("Size of training data set %d" % (i + 1))

    print(border)
    print("Testing data set")
    print(border)
    for i in range(len(Data_test)):
        print("ID: %d,Feature %s, Label %s" % (i, Data_test[i], Target_test[i]))
        print("Size of testing data set %d" % (i + 1))

    Classifier = MarvellousKNeighborsClassifier()

    Classifier.fit(Data_train, Target_train)

    Predictions = Classifier.predict(Data_test)

    Accuracy = accuracy_score(Target_test,Predictions)

    return Accuracy

    dataset = load_iris()

    data = dataset.data
    target = dataset.target

    print(border)
    print("Actual data set")
    print(border)

def main():
    Accuracy = MarvellousML()
    print("Accuracy of classifier algorithm with K neighbor classifier is : ",Accuracy * 100,"%")

if __name__ == "__main__":
    main()