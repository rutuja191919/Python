#import required library
from sklearn import tree

#Load the dataset
#Rough  1        One hot encoding
#Smooth 0

#Cricket 2
#Tennis  1

def MarvellousML(weight,surface):

    BallsFeatures = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    Names = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    #Decide the Machine Learning Algorithm
    obj = tree.DecisionTreeClassifier()

    #Perform the training of model
    obj = obj.fit(BallsFeatures, Names)   #Training

    #Perform the testing
    result = obj.predict([[weight,surface]])   #Testing

    if result == 1:
        print("Your object looks alike Tennis Ball")
    elif result == 2:
        print("Your object looks alike Cricket Ball")

def main():
    print("---------------Marvellous Infosystems by Piyush Khairnar---------")

    print("Enter the weight of object")
    weight = input()

    print("What is the surface type of your object Rough or Smooth")
    surface = input()
    if surface.lower() == "rough":
        surface = 1
    elif surface.lower() == "smooth":
        surface = 0
    else:
        print("Error : Wrong input")
        exit()

    MarvellousML(weight,surface)

if __name__ == "__main__":
    main()