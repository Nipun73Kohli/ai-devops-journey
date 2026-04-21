# # write a program to print multiplication table of a given number using for loop 
i = int(input("Enter the number for which you want to print the multiplication table "))
for k in range(1,11):
     print(f"{i} * {k} = {i*k}")

# # Write a program to greet all the person names stored in a list l and which starts with S

l = ["Harry","Soham","Sachin","Rahul"]

for i in l:
    if(i.startswith("S")):
        print(f"Hello {i}")

# # write a program to print multiplication table of a given number using while loop

i = int(input("Enter the number for which you want to print the multiplication table"))
k =1
while k<=10:
    print(f"{i} * {k} = {i*k}")
    k += 1

# # write a program to find whether a given number is prime or not 

i = int(input("Enter the number of want to find is prime or not "))
for k in range(2, i):
    if i% k ==0:
         print("The number is not prime")
         break
else:
    print("The number is prime")

# # Write a program to find the sum of first n natural numbers using while loop 

i = int(input("Enter the value of n "))
k = 0
sum = 0
while k <=i:
    sum += k
    k += 1

print(f"The sum of first n natural numbers is {sum}")

# Write a program to calculate the factorial of a given number 

i = int(input("Enter the number of want to calculate factorial of "))
fact = 1
for n in range(1,i+1):
    fact *= n
    n += 1
print(f"Factorial of {i} is {fact}")

# Write a program to print the following star pattern 

'''
  *
 ***
*****  for n = 3 

'''

n = int(input("Enter the value of n"))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("") # To Print new line 

# Write a program to print the following star pattern 

'''
*
**
*** n = 3
'''
n = int(input("Enter the value of n"))
for i in range (1,n+1):
    print("*"*i, end = "")
    print()

# Write a program to print the following star pattern 

'''
***
* *
***

'''

n = int(input("Enter the value of n "))

for i in range(1,n+1):
    if (i == 1 or i == n):
        print("*"*n)
    else :
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print()   

