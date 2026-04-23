f = open("day4-file-I/O/file.txt")
# data = f.readline()

# print(data,type(data))

# line1 = f.readline()
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()
# print(line3,type(line3))

# line4 = f.readline()
# print(line4,type(line4))

# We can also use loops to print the lines 

line = f.readline()

while (line!= ""):
    print(line)
    line = f.readline()
f.close()

# f = open("day4-file-I/O/MYfile.txt","w")
# f.write("Hello this is an example of writting a line")
# f.close()