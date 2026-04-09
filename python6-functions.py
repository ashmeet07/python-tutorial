a,b=10,20

#Normal Function
def hello_world():
    print("Hello World!")


#return type function
def add(a,b)->int:
    return a+b

#return function
def hello_world():
    return "Hello World!"


#argument function
def add(*args):
    return sum(args) #use * args when need to unpack or print or return multiple values


#keyword argument function
def listofemp(**kwargs):
    return kwargs #cannot use ** kwargs too many value to unpack error


#default argument function
def add(a:int,b=0):
    return a+b



#In memory function store not leave for next one
a=lambda a,b:a+b 


