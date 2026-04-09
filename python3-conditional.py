input=10

#Single line if else
print(input if input%3==0 else 10)

#If statement
if input%10==0:
    print("Input value modulo of 10")



#if-else statement
if input%3==0:
    print("Input value is modulo of 3")
else:
    print("Input value is not modulo of 3")


#if elif-else statement
if input%3==0:
    print("Input value is modulo of 3")
elif input%10==0:
    print("Input value modulo of 10")
else:
    print("Input value is not modulo of 3")


#Nested if elif else:- Look by your self


#assert for testing in pytest
assert input>=10, "Input must be 10 or greater"


#Match case like switch

match input:
    case input if input==1:
        print("Input is divisible by 1")
    case 2:
        print("Input is divisible by 2")
    case _ :
        print("Input is greater than 2")    