'''
Create a rock, paper and scissors game 

1 Rock 
-1 Paper 
0 Scissors

'''


import random

computer = random.choice([1,0,-1])
user_choice = input("Please enter your choice from Rock, Paper and Scissorrs ")
user_dict = {"Rock":1, "Paper": -1, "Scissors": 0}
user = user_dict[user_choice]

computer_dict = {1:"Rock", -1:"Paper", 0:"Scissors"}
print(f"You Chose {user_choice} and computer chose {computer_dict[computer]}")
if computer == user:
    print("It is a draw")
else:
    if computer == 1 and user == -1:
        print("You won")
    elif computer == 1 and user == 0:
        print("You lose")
    elif computer == -1 and user == 1:
        print("You lose")
    elif computer == -1 and user == 0:
        print("You Won")
    elif computer == 0 and user == 1:
        print("You Won")
    elif computer == 0 and user == -1:
        print("You lose")
