#Python Exception

a=10
b=0

try:#Try block to raise exception
    a/b
except ZeroDivisionError as e:#except to catch and tell to the user
    print(e,"Divided by 0 Error")

finally:#always executes
    print("Success fully catch the exception")


#Custom Exception

class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is less than {amount}")# if not call the object act as instance and show variables of instance of the class


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)



try:
    withdraw(1000, 2000)
except InsufficientBalanceError as e:
    print(e)
