# While loop 
 # while(condition): This block keeps executing until the condition is true 
# Body of the loop 

# If the loop is entered, the process of [condition check and execution] is continued until the condition becomes false 

# write a program to print 1 to 50 using while loop 

# i = 1
# while(i<51):
#     print(i)
#     i+=1


# print the elements of the list using while loop 

# list1 = ["Hello","How are yaa","G'Day Mate","Ciao","Good on ya"]
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i+=1

# for loops 

l = [1,2,33,44,12,45]
for i in l:
    print(i)

# using range function with for loops 

for i in range(1,6):
    print(i)

# For loop with else condition 

l = [7,9,10]

for i in l:
    print(i)
else:
    print("done")

# Using break and continue statements 

for i in range(100):
    if(i==5):
        break
    print(i)
    
for i  in range(10):
    if(i==3):
        continue
    print(i)
    