# While loop
x = 5
while x >= 0:
    print(x, end=" ")
    x -= 1

print("\n")

# For loop
x = 5
for _ in range(x):
    print("*", end="")

print("\n")

# Nested for loop
for i in range(x):
    for j in range(x):
        print("*", end="")
    print()

# For-else loop
for i in range(x):
    if i == 10:
        break
    print(i)
else:
    print("Loop Successfully executed")
