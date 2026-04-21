# write a program to find greatest of three numbers 

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c 

a = int(input("Enter the value of first number "))
b = int(input("Enter the value of second number "))
c = int(input("Enter the value of third number "))

print(f"The greatest number is {greatest(a,b,c)}")


# Write a program to convert F to celcius

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter the value of temprature in F "))

print(f"The value of temprature in celsius is {round(f_to_c(f),2)} ")

# write a recursive function to calculate the sum of first n natural numbers

def rec_sum(a):
    if(a==1):
        return 1
    return a+rec_sum(a-1)
a = int(input("Enter the value of n: "))

print(f"The sum of first n natural numbers is {rec_sum(a)}")

# Write a python function to print first n lines of the following pattern 

'''
***
**
*
'''

def pattern(n):
    for i in range(n,0,-1):
        print(f"*"*i)
pattern(3)

# Write a python function to remove a given word from a list 



def rem(l,word):
    for item in l:
        l.remove(word)
        return l 
l = ["Good","god","mod","mode","made"]   
print(rem(l,"mod"))

# Write a python function to print multiplication table of a given number 

def table(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i} ")
n = int(input("Enter the value of n for which you want to print the table "))

table(n)