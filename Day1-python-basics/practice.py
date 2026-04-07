# Strings 
# write a python program to display a user entered name followed by good afternoon using input() function.
name = input("Enter your name ")
print(f"Good Afternoon, {name}")

#write a program to fill in a letter template given below with name and date.

letter ='''Dear <|Name|>, 
           You are selected! 
           <|Date|>'''
print(letter.replace("<|Name|>",name).replace("<|Date|>","17 March 2026"))

#Write a python program to add two numbers

a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))

print("The sum of a and b is ", a+b)

#write a python program to find remainder when a number is divided by z 

a = 84
z= int(input("Enter the value of z "))
print("The value of remainder is ",a%z)

#Use comparison operator to find out whether a given variable a is greater than b or not. take a = 34 and b = 80 as an example

a = 34
b = 80 

print("is a greater than b ? ", a>b)

#write a python program to find an average of two numbers entered by the user.

a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
print("Average of the two entered numbers is ",(a+b)/2)

#write a python program to calculate the square of a number entered by the user 

a = int(input("Enter the value of the number you want to find square of "))
print("Square of the entered number is ",a*a)

a = int(input("Please enter your age "))
if(a>18):
    print("You are above the age of consent")
elif(a<0):
    print("You have entered a negative age which is invalid")
elif(a==0):
    print("You have entered 0 which is an invalid age ")
else:
    print("You are below the age of consent ")

#Write a program to print yes when the age entered by the user is greater than or equal to 18 

age = int(input("Enter your age"))
if(age>=18):
    print("Yes")
else:
    print("no")

#Dictionary 
#write a program to create a dictionary of hindi words with value as their english translation. Provide user with an option to look it up 

words = {"madad":"help","sabar":"patience","darr":"fear"}
word = input("Enter the word you want to know meaning of ")
print(words[word])

d = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d)

#Sets

#write a program to input eight numbers from the user and display all the unique number once

s = set()
s.add(input("Enter the value of number 1 "))
s.add(input("Enter the value of number 2 "))
s.add(input("Enter the value of number 3 "))
s.add(input("Enter the value of number 4 "))
s.add(input("Enter the value of number 5 "))
s.add(input("Enter the value of number 6 "))
s.add(input("Enter the value of number 7 "))
s.add(input("Enter the value of number 8 "))

print(s)

#can we have a set with 18(int) and '18'(str) as a value in it - yes

s = {18,"18"}
print(s)
print(type(s))

#what will be the length of the following set s - 2 because 20 = 20.0

s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(len(s))

#Tuples 
#write a program to store seven fruits in a list entered by the user
a = []
f1 = input("Enter the name of first fruit ")
a.append(f1)
f2 = input("Enter the name of first fruit ")
a.append(f2)
f3 = input("Enter the name of first fruit ")
a.append(f3)
f4 = input("Enter the name of first fruit ")
a.append(f4)
f5 = input("Enter the name of first fruit ")
a.append(f5)
f6 = input("Enter the name of first fruit ")
a.append(f6)
f7 = input("Enter the name of first fruit ")
a.append(f7)
print(a)

#write a program to accept marks of 6 students and display them in a sorted manner

marks =[]
m1 = int(input("Enter the marks of first student "))
marks.append(m1)
m2 = int(input("Enter the marks of first student "))
marks.append(m2)
m3 = int(input("Enter the marks of first student "))
marks.append(m3)
m4 = int(input("Enter the marks of first student "))
marks.append(m4)
m5 = int(input("Enter the marks of first student "))
marks.append(m5)
m6 = int(input("Enter the marks of first student "))
marks.append(m6)
print(marks.sort())

#check that tuple type cannot be changed in python

a = (34,234, "harry")
a[2] = "Larry"

#write a program to sum a list with 4 numbers
list1 = [23,45,12,32]
print(sum(list1))

#write a program to count the number of zeroes in the following tuple 

a = (7,0,8,0,0,9)
print(a.count(0))

#Write a program to find greatest of four numbers entered by the user 

a = int(input("Enter the value of number 1 "))
b = int(input("Enter the value of number 2 "))
c = int(input("Enter the value of number 3 "))
d = int(input("Enter the value of number 4 "))

if(a>b and a>c and a>d):
    print(" a is the greatest number out of 4")
elif(b>a and b>c and b>d):
    print(" b is the greatest number out of 4")
elif(c>a and c>c and c>d):
    print("c is the greatest number out of 4")
else:
    print("d is the greatest", d)

#write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user 

marks_1 = int(input("Enter the marks of subject 1 "))
marks_2 = int(input("Enter the marks of subject 2 "))
marks_3 = int(input("Enter the marks of subject 3 "))

total_marks = marks_1+marks_2+marks_3
total_perc = (total_marks/3)

if(total_perc>40 and marks_1>33 and marks_2>33 and marks_3>33):
    print("Student has passed the exams")
else:
    print("Student has failed the exams")    

#A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". write a program to detect these spams
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment: ")

if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("The message is a spam")
else:
    print("The message is not a spam")

#write a program to find whether a given username contains less than 10 characters or not 
username = input("Enter your username ")

if(len(username)<10):
    print("Your username contains less than 10 characters")
else:
    print("All is well!")

# Write a program which finds out whether a given name is present in a list or not 

l = ["Harry","Rohan","Shubham","Divya"]

name = input("Enter your name ")

if(name in l):
    print("Your name is in the list")
else:
    print("Your name is not in the list")