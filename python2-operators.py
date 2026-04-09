#Operators in python

#Arithmetic Operators
a,b=10,20
print(a/b)#Float Division
print(a//b)#Floor Division
print(a+b)#Add
print(b-a)#Subtract
print(a*b)#Multiplilcation
print(a**b)#Power
print(b%a)#Remainder

#Comparision Operator
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

#Assignment Operator
a+=1
b-=1
a*=1
b/=19
b=a
print(a,b)

#Logical Operator
print(a and b)
print(b or a)
print(not a)


#Membership Operator
string="python"
print('p' in string)
print("t" not in string)

#Bitwise Operator
print(a & b)
print(a | b)
print(a<<1)
print(b>>2)
print(a^b)
print(~a)


#identity operator
import copy 
a=10
b=copy.copy(a)
print(a is b)


#ternary operation
a=a if a>0 else b