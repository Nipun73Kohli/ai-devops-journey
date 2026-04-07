# we can write strings in three ways 
a = 'string'
b = "string"
c = '''string''' 

# string is immutable 
# string in python can be sliced for getting a part of the strings 

#consider the following String name = "harry" => length = 5
#                                      01234
#To slice the string we use the following syntax 

# sl = name[ind_start:ind_end]

# sl[0:3] return characters from 0 to 3 index,3 will not be included

# we can provide a skip value as a part of our slice as well like this :
# word = "amazing"
#word[1:6:2] #mzn 
# a = "0123456789"
#a[1:7:3] # 14

# Methods to use with strings 
name = "harry"
print(len(name))
print(name.endswith("rry"))
print(name.startswith("ha"))

# escape characters 
#\n is an escape character which is used to print new line 

a = "Harry is a good boy\nbut not a bad boy"
print(a)

# Dictionary 
marks = { "Harry" :100, "Shubham": 56, "Rohan": 23

}
print(marks["Rohan"])
marks.update({"Harry":99})
print(marks["Harry"])

print(marks.get("Harry2")) # Prints none
print(marks["Harry2"]) # returns an error

# Lists

# Lists are mutable 
# .append adds an element at the last of the list

# .insert adds an element at a particular index of the list for example
 
l1 = [1,34,62,2,6,11]
l1.insert(2,333) # Insert 333 such that it's index in the list is 3
print(l1)
print(l1.pop(2)) # deletes the value at index 2 and returns the value removed from the list 
l1.remove(62) # will remove 62 from the list
print(l1)

# Sets 
# sets is a cllection of non repetitive elements

s = {1,5,32}

e = set() # don't use s ={} as it will create an empty dictionary 
s.add(56)
print(s)

# you cannot access sets with index

# Tuples 

# tuple is an immutable data type in python 
a = () # it is an empty tuple
b = (1,) # it is a tuple with single element  
d = (1,45,342,4343,False,"Rohan","Shivam")

#Tuple methods 
d = (1,45,342,4343,False,"Rohan","Shivam")
a = d.count(45) # returns the value of number of times the element is present in the tuple
print(a)
c = d.index(342) # returns the index of first occurence of the element
print(c)