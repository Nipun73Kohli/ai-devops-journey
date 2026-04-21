# Function definition
def avg():
    a =int(input("Enter your number 1: "))
    b =int(input("Enter your number 2: ")) 
    c =int(input("Enter your number 3: "))
    print((a+b+c)/3)

# Function call
avg()

# write a program to greet Good day to a user 

def greet(user):
    print(f"Good day {user}")

user = input("Please enter your name ")

greet(user)

# Default arguments in function 

def greet2(name,ending= "Thanks"):
    print(f"Good day {name}")
    print(ending)

name = input("Enter your name ")
greet2(name) # In this function call we have not passed the value of ending so it is going to use the default value

greet2(name,"Thank you ") # here we have passed the value of ending which is going to replace the defalut value