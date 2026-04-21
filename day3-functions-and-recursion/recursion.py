# Recursion is a function which calls itself

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2*1
factorial(3) = 3*2*1
factorial(4) = 4*3*2*1
factorial(5) = 5*4*3*2*1

factorial(n) = n*factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n = int(input("Enter the value of number you want a fictorial of: "))
print(f"The factorial of the number is: {factorial(n)} ")