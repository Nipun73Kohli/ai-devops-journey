import random
# Write a program to read the text from a given file "poems.txt" and find out whether it contains the word twinkle 

with open("day4-file-I/O/poems.txt") as f:
    content = f.read()
    if "twinkle" in content:
        print("Yes the word twinkle is present in it")
    else:
        print("No the word is not present in it ")

# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file "Hi-score.txt" which is either blank or conttains the previous high score. You need to write a program to update the hi-score whenever the game() function breaks the hi-score

def game():
    print("You are playing a game")
    score = random.randint(1,78)
    print(f"Your score is {score}")
    with open("day4-file-I/O/Hi-score.txt") as h:
        current_high_score = h.read()
        if(current_high_score!=""):
           current_high_score = int(current_high_score)
        else:
            current_high_score = 0
    if(score>current_high_score):
        with open("day4-file-I/O/Hi-score.txt","w") as h:     
            h.write(str(score))  
    return score

game()

