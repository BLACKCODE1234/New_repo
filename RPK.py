# masa masa masa as old as you're, you're still doing hello world😂
print('Hello World')
print('just pulled to push')
# Just pushing something here, try to see if it is nice


import time  # import the time module to keep track of the game
# and manages the user time for a question

import random # import the random module to help shuffle the items 

import os # to save the number of users and their scores - an addtitional something
# can be replaced by a database

print("A ROCK,SCISSORS,PAPER GAME.")  # print the header of the game
username = input("USERNAME: ").capitalize() # takes the name of the user

ITEMS = ["rock","scissors","paper"]  # container of the game variables
# print(computer)

print("Guide to the Game") # this print the rules of the game
print("PICK A CHOICE TO PLAY, YOU HAVE THREE SHOT.\n" 
    "A CORRECT GAME GIVES YOU 3 POINTS,\n" 
    "A MISTAKE SUBTRACT 3 POINTS FROM YOUR TOTAL\n",
    "FAILURE TO ANSWER WITHIN THE SAID TIME DEDUCT 5 POINTS.")

game_question = input(f"{username},Do you want to play(Y/N): ").upper() #ask if user wants to play

if game_question == "Y": # if user chooses yes 
    print(f"{username},welcome to the game......") #this is printed out 


    score = 0
    count = 0
    total_count = 4
    total_score = 12
    while True: # ensures the game is  in a loop
        computer = random.choice(ITEMS)  # the computer chooses an item randomly

        score +=0
        count = count + 1
        if count == total_count:
            print("You have exhausted all attempt\n"
                  "Loging out... ")
            break
        user_question = input("Type your choice: ").lower().strip()
        if user_question == computer:
            score = score
            print("It's a tie")
        elif user_question == "rock" and computer == "scissors":
            score = score +3
            print(f"{username}, Wins.")

        elif user_question == "rock" and computer == "paper":
            score = score - 3
            print("Computer, Wins.")

        elif user_question == "paper" and computer == "scissors":
            score = score - 3
            print("Computer, Wins.")

        elif user_question == "paper" and computer == "rock":
            score = score +3
            print(f"{username}, Wins.")

        elif user_question == "scissors" and computer == "rock":
            score = score +3
            print(f"{username}, Wins.")  

        elif user_question == "scissors" and computer == "paper":
            score += 3
            print(f"{username}, Wins.")
 
        
        
elif game_question == "N": # if user chooses no
    print(f"{username},Thank you.Goodbye!!!") # this is printed out
    # break
else: # if user takes anything apart from the Y/N,user is denied
    print("Invalid entry.") # this is printed out

"""I AM NOT DONE SO ADD MORE
ADD THE TIME OR /// FEATURE TO IT"""