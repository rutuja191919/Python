import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):
    #Load data
    data = pd.read_csv(data_path,index_col = 0)

    print("Size of actual dataset",len(data))

    #Clean, Prepare and manipulate data
    feature_names = ["Whether","Temperature"]

    print("Names of features",feature_names)

    weather = data.Whether
    temperature = data.Temperature
    play = data.Play

    #Creating labelEncoder
    le = preprocessing.LabelEncoder()

    #Converting string labels into numbers
    weather_encoded = le.fit_transform(weather)
    print(weather_encoded)

    #Converting string into numbers
    temp_encoded = le.fit_transform(temperature)
    label = le.fit_transform(play)

    print(temp_encoded)

    #Converting weather and temp into single listof tuples
    features = list(zip(weather_encoded,temp_encoded))

    #Train data
    model = KNeighborsClassifier(n_neighbors = 3)

    #Train model using the training sets
    model.fit(features,label)

    #Test data
    predicted = model.predict([[1,2]]) # 0 : Overcast 2 : Mild
    print(predicted)

def main():
    print("----Marvellous Infosystems --------")

    print("Machine Learning Application")

    print("Play predictor application using K Nearest neighbor algorithm")

    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()
