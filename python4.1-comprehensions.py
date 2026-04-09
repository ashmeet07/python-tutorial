#Python list, dict  generators comprehensions


#List comprehensions
a=[i for i in range(10)]
b=sum(i for i in range(10))

#nested
a=[(i,j) for i in range(10) for j in range(10)]

print(a,type(b))

#dict comprehensions
a={i:i for i in range(10)}
b=dict({i:i for i in range(10)})

print(a,type(b))

#Generator comprehensions
a=(i*i for i in range(10))
print(a)#lazy memory evaluation