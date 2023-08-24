# Use of Collection data type in python : List, Set, Tuple, Dictionary
# List Demo : indexed datatype, heterogeneous

values = [10,20,30,40]

print(values)

print(type(values))

print(len(values))

values.insert(2, 11)  #insert at any position
print("Data after insert")

values.insert(15,89)  #insert works as append with inserting at any index
print("Size of list is now : ",len(values))
print("Data after insert 15 is : ",values)

print(values[0])
print(values[1])
print(values[2])
print(values[3])

values.append(50)  #appending at last

print(values)

values.remove(20)

print(values)

values.append(50)

print(values)

print(type(values[0]))

values.append(90.89)

print(values)


