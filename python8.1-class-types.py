from abc import ABC, abstractmethod


#Class with no method
class No_Method():
    pass


#class with one static method
class One_Method():
    @staticmethod #have no self argument on method declaration
    def print_hello():
        return "Hello World"
    

#class with single constructor
class My_Class:
    def __init__(self):
        pass


#class with class method
class Class_Method:
    x=10
    @classmethod
    def add(cls):
        return cls.x+1
    
#class with abstract method
class Abstract(ABC):
    @abstractmethod
    def add(self):
        if not isinstance(self,Abstract):
            NotImplemented
    
    def __add__(self,other):
        return self.x+other.x
    

