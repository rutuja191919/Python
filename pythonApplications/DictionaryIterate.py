Batches = {"PPA" : 18000, "LB" : 16700, "Python" : 16500, "Angular" : 15000}

print("Data of Dictionary : ",Batches)

print("Data traversal using the loop")
for x in Batches:
    print(x)

print("Data traversal using the loop")
for x in Batches:
    print(x,Batches[x])

print("Data traversal using the loop")
for x in Batches:
    print(x,Batches.get(x))

keyBatches = Batches.keys()
print(type(keyBatches))     #dict_keys : list
print(keyBatches)

valueBatches = Batches.values()
print(type(valueBatches))    #dict_values : list       1:1 association is there in between keys and values
print(valueBatches)

#for i in range(0,len(Batches)):
    # print("Batch name is : ",keyBatches[i]," Value is : ",valueBatches[i])    #error as dict_keys and dict_values are not subscriptable