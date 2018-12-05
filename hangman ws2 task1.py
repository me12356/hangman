#Name: Hangman game
#Description: Allows users 
#Author: Alia
#Date: 28/1/2018
#Version:1

#title of the game
print ("Hangman Game")

#importing the time module
import time

#welcoming the user
name = input("what is your name? ")

print ("Hello, " + name," Lets play hangman!")

#wait for 1 second
time.sleep(1)
print ("Start guessing...")
time.sleep(0.5)

#now we set the secret word
word = "secret"

#creates a variable with an empty value
guesses = ""

#determine the number of turns
turns = 10

#create a while loop
#check if the turns are more than zero
while turns > 0:
    #make a counter that starts wth zero
    failed = 0
    #for every character in secret_word
    for char in word:
    #see if the character is in the players guess
        if char in guesses:
        #print then out the character
            print

        else:
         #if not found, pprint a dash
            print ("_"),
         #and increase the failed counter with one
            failed += 1
        #if failed is equal to zero
        #print You Won
            if failed == 0:
                print ("You Won")
        #exit the script
                break

            print

        #ask the user to guess a character
        guess = input("guess a character:")

        #set the players guess to guesses
        guesses += guess

        #if the guess is not found in the secret word
        if guess not in word:

            #turns counter drecreases with 1 (now 9)
            turns -= 1

            #print wrong
            print ("wrong")

            #how many turns left
            print ("you have", + turns, "more guesses")

            #if the turns are equal to zero
            if turns == 0:
                #print "you lose"
                print ("You Lose")

            
            
            
            

