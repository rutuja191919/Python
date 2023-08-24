print("Demonstration of Dictionary")

# Data : Heterogeneous
# Ordered : Yes
# Indexed : No          there is a key in dictionary
# Mutable : Yes
# Duplicated : No       key : no , value : yes

programming = {"C" : "Richie", "C++" : "Stroustrup", "Java" : "Gosling", "Python" : "Rossum","C" : "Thomson"}
Batches = {"PPA" : 18000, "LB" : 16700, "Python" : 16500, "Angular" : 15000}

print("Data of dictionary : ",Batches)
print("Data type is : ",type(Batches))
print("Length of dictionary is : ",len(Batches))
print("Values of PPA is : ",Batches["PPA"])

print(programming)  #duplicate key gets replaced with the new value of the key