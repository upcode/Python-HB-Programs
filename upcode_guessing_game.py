#write a program guess number between 1 and 100
#ask user to guess the number(give them hint if its high or low)

#psedocode outline of guessing game program
#greet player
#get player name
#choose random number between 1 and 100
#while True:
    #get guess
    #if guess is incorrect
        #give a hint
    #else:
        #congrualte player
import random

computer_number = random.randint(1, 100)
print computer_number


#print a string that greets user to guessing game
print "Welcome to the Guessing Game"
#created player_name and binded it to raw_input
player_name = raw_input("what is your name?: ")
#welcome player to the guessing game
print "Welcome %s to the Guessing Game" % (player_name)
#choose a number between 1-100
player_guess = int(input("Pick a number between 1 and 100 (1-100): "))
#create a while loop with given conditions
while True:
    if player_guess > computer_number:
        print "GUESS IS TO HIGH!, please try again"
        player_guess = int(input("Pick a number between 1 and 100 (1-100): "))
    elif player_guess < computer_number:
        print "Guess IS TO LOW!, Please try again"
        player_guess = int(input("Pick a number between 1 and 100 (1-100): "))
    else:
        player_guess == computer_number
        print "YOUR GUESS WAS CORRECT!"
        break

print "Thanks for playing!"