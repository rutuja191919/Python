print("Demonstration of list")

# You can take value from user

# Data : Heterogeneous
# Ordered : Yes
# Indexed : Yes
# Mutable : Yes
# Duplicated : Yes

data = [11,21,51,101,21,11]

data1 = [11, 90.80, True, "Hello"]  #Heterogeneous

print("Data is heterogeneous : ",data1)
print("Data is ordered : ",data1)
print("Data with duplicate elements : ",data)
print("Data at index 2 : ",data[2])

print("List is mutable")
data.append(201)  #insert : shift honar at position if inserting at some pos
print("Data after append : ",data)
data.pop()  #remove : remove by position pop : remove last
print("Data after pop : ",data)


