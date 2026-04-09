#Python Encapsulation


#Protected data member
class Protected:
    def __init__(self):
        self._x=10

#Private data member
class Private:
    def __init__(self):
        self.__x=10 #python internally changes _Private__x so you can access using this namespace


#Accessing the private protected values form class

class Encapsulation:
    def __init__(self):
        self.__amount=1000
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self,amount):
        if amount>0:
            self.__amount=amount