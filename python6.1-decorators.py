# 3Passing Function as Argument
def say_hello():
    print("Hello")

def caller(func):
    func()

caller(say_hello)



#Decorator
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


# def hello():
#     print("Hello World")

# hello = my_decorator(hello)
# hello()


@my_decorator
def hello():
    print("Hello")


hello()

def para_deco(n):
    def my_decorator(func):
        def wrapper():
            print("Before function")
            func()#Use loop to iterate n time function
            print("After function")
        return wrapper
    return my_decorator


@para_deco(3)
def hello_world():
    print("Hello")

hello_world()