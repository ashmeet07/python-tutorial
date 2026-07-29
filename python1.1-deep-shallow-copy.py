import copy

#Shallow copy any change in b reflects in a
a=[1,2,3,4]
b=a
b.append(10)
print(id(a),id(b))


#Deep copy change in b will not affect a because create copy of the object
a=[1,2,3,4]
b=copy.deepcopy(a)
b.append(10)
print(id(a),id(b))
