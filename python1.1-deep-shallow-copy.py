import copy

#Shallow copy any change in b reflects in a
a=int(input("Enter any number"))
b=copy.copy(a)


#Deep copy change in b will not affect a because create copy of the object
a=int(input("Enter any number"))
b=copy.deepcopy(a)