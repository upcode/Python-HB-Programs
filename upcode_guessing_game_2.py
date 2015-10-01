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

print "WELCOME TO THE GUESSING GAME!"
player_name = raw_input("What is your name?: ")  #user enters their name
print "Glad you could join us %s! on our guessing adventure, lets get started!" % (player_name)
print "To play the guessing game, please pick a number between 1-100."
print " %s you get 5 tries to guess my number." % (player_name)
print "Good Luck %s, may the force be with you!" % (player_name)
player_guess = int(input("Guess a number between 1-100: "))  # user guess number between 1-100

number_of_guesses_player_gets = 5  # number of guesses user gets
player_guess_counter = 0  # this is start of the counter at 0

while player_guess_counter < 5:  # while guess are less then 5, loop will continue
    if player_guess < computer_number:  # player guess is greater then number
        print "Guess IS TO LOW"
        print "Please guess again"
        player_guess = int(input("Please pick a number between 1-100: "))  #user re-guesses
        player_guess_counter += 1  # everytime user guess number the counter will increase by one
    elif player_guess > computer_number: #player guess is greater then computer number
        print "GUESS IS TO HIGH"
        print "PLease guess again"
        player_guess = int(input("Please pick a number between 1-100: "))
        player_guess_counter += 1
    elif player_guess == computer_number:  # if players guess is same as computer number
        print "NICE JOB %s, YOU ARE A ROCK STAR!" % (player_name)
        print "Thanks for playing %s, we hope you come back and play again soon!" %(player_name)
        break
else:
    print("Sorry, you ran out of guesses! The Galxay is doomed!")
