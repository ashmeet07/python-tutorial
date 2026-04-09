#Iterators Generators

a=iter([1,2,3,4])
print(a.__next__())
print(a.__next__())
print(a.__next__())



#Generators uses yield
def display():#Generator Function
    i=10
    while(i<=20):
        yield i
        i+=1

for i in display():#Iterator
    print(i)

print(next(display()))