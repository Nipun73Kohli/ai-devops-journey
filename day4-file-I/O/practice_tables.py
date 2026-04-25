# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. place these files in a folder for a 13 year old

def generateTable(n):
    table = ""
    for items in range(1,11):
        table += f"{n} X {items} = {n*items}\n"
    with open(f"day4-file-I/O/tables/table{n}.txt","w") as f:
         f.write(table)    
for i in range(2,21):
        generateTable(i)
