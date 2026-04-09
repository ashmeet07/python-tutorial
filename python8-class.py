#Python Class

class MyPython():
    #Constructor
    def __init__(self,val):
        self.x=val

    def __str__(self):#This method runs always
        return  "This is my method using print function"

    def __repr__(self):
        return f"MyPython(val={self.x})"


obj=MyPython(10)

obj
print(obj)