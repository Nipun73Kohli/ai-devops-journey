# A file contains a word "Donkey" multiple times. You need to write a program which replaces the word with ##### by updating the same file 
word = "donkey"
with open("day4-file-I/O/practice3.txt") as f:
    content = f.read()

contentNew = content.replace(word,"#####")

with open("day4-file-I/O/practice_3.txt","w") as f:
    f.write(contentNew)
    
# Repeat the above problem for list of uncensored words

words = ["shitty", "damn", "mess", "damn", "pissed"," bullshit"]

with open("day4-file-I/O/practice_3a.txt") as f:
    content = f.read()
for word in words:
        content = content.replace(word,"#"*len(word))

with open("day4-file-I/O/practice_3a.txt","w") as f:
    f.write(content)






