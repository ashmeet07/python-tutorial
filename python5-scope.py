#LEGB

"""
Local
Encoding 
Global
Built-in 
"""
# Functionality provided by python


x=10#Global

def print_value():

    #call global variable using global keyword

    global x
    b=20#nonlocal

    def print_val():
        c=30#local
        nonlocal b
        print(b)
        
    print(x,b)