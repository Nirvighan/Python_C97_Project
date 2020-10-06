#IMPORT RANDOM
import random

#GIVE THE HEADING
print("WELCOME TO GUESSING GAME")

#CREATE A VARIABLE AND SET RANDOM VALUE TO IT FROM 1TO 9
rand = random.randint(1,9)

#CREATE THE CHANCE VARIABLE
chances = 0

#SHOW TEXT WHAT TO DO
print("GUESS A NUMBER BETWEEN 1 To 9")


#RUN A WHILE LOOP 
while chances<5:
    #TAKE USER INPUT
    guess = int(input("ENTER THE NUMBER TO GUESS"))

    #WRITE THE CONDITION IF GUESS IS CORRECT
    if guess == rand:
        print("CONGRATS! YOU GUESSED IT RIGHT")
        break
    
    # WRITE THE CONDITION TO GIVE HINT
    elif guess < rand:
        print("YOUR GUES IS TOO LOW")
        print("GUESS A NUMBER HIGHER THAN THIS")

    else:
        print("YOUR GUESS IS TOO HIGH.")
        print("GUESS A NUMBER LESS THAN THIS")
    
    #EVERY IME LOOP RUNS LESS 1 CHANCE
    chances+=1

#WRITE THE CONDITION FOR LOSE
if chances==5 and guess!= rand:
    print("YOU LOSE")

    