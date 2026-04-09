from abc import ABC, abstractmethod


#class with abstract method
class Abstract(ABC):
    @abstractmethod
    def add(self):
        pass




class Number(Abstract):
    def __init__(self, x):
        self.x = x

    def add(self, other):
        return self.x + other.x

    def __add__(self, other):
        if not isinstance(other, Number):
            return NotImplemented
        return self.x + other.x
