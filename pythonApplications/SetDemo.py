print("Demonstration of Set")

# Data : Heterogeneous
# Ordered : No
# Indexed : No           There is no index as order of insertion is not there
# Mutable : Yes          for immutable there is frozen set
# Duplicates : No

data = {11,21,51,101,11,21}         #error is not there as it doesnt store duplicate element
data1 = {11, 90.80, True, "Hello"}  #Heterogeneous

print("First set data : ",data)
print("Length of data : ",len(data))
print("Data is heterogeneous : ",data1)
print("Data is unordered : ",data1)
# print("Data at index 2 : ",data[2])    #you cannot use subscript operator
print("Data with unique elements : ",data)

print("Set is mutable")
# Insert element in set
data.add(211)
print("Data after insertion : ",data)

#remove element from set
data.remove(211)
print("Data after removal : ",data)

data.discard(201)              #remove the element from the set but if element is not there then it does nothing does not give exceptipn
print("Daya after discard : ",data)
