#we have factorial in math program

# Factorial in math module
# factorial using recursion
# factorial using iterative

# Factorial in math module
# import math
# n = int(input("number"))
# result = math.factorial(n)
# print ("factorial of ", n, "is", result)


# factorial using recursion, recursion means function call its self
# there are two parts 1 base case 2 recursive case

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
n = int(input("enter the number : "))
result = fact(n)
print("factorial of " , n , "is ", result)
