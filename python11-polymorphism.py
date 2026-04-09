#In python polymorphism has two types compile-runtime


#compile time/method overloading is not achievable in python by default we use arguments to achieve that 


#Method overloading using singledispatch regestration

from functools import singledispatch

@singledispatch
def add(a, b):
    raise NotImplementedError

@add.register
def _(a: int, b: int):
    return a + b

@add.register
def _(a: str, b: str):
    return a + b

#Method overloading using argument function
def add(*args):
    return sum(args)


add(10,20)
add(10.2,30.5)



#Runtime Overriding it achieve by default in python

class Vehicle:
    def show(self):
        print("This is my Car")
    
class Bike(Vehicle):
    def show(self):
        print("This is my Bike")
    

print(Bike.mro())