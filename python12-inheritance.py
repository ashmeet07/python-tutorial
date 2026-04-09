#Single Inheritance

class First:
    def __init__(self):
        pass

class Second(First):
    def __init__(self):
        pass

#You can call first class method using second class objets

#Multiple Inheritance
class First:
    def __init__(self):
        pass

class Second():
    def __init__(self):
        pass

class Third(First,Second):
    def __init__(self):#Confusing when parent classes having same methods
        pass


#Multi-level Inheritance
class First:
    def __init__(self):
        pass

class Second(First):
    def __init__(self):
        pass

class Third(Second):
    def __init__(self):#Confusing when parent classes having same methods
        pass



#Hybrid Inheritance

class First:
    def __init__(self):
        pass

class Second(First):
    def __init__(self):
        pass

class Third(First):
    def __init__(self):#Confusing when parent classes having same methods so properly use super and sovle using mro tracing
        pass

class Fourth(Second,Third):
    def __init__(self):#Confusing when parent classes having same methods
        pass



#MRO
print(Fourth.mro())
# [<class '__main__.Fourth'>, <class '__main__.Second'>, <class '__main__.Third'>, <class '__main__.First'>, <class 'object'>]
