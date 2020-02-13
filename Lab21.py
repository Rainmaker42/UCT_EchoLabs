'''
Flow control lab
Higher / Lower guessing game
Psudocode:
Preprocessing directive to include the random library
Declare and assign variable answer to be a random number in the range 0-100
Declare and assign variable guesses to store number of guesses
Declare and assign variable input to store user input
While input is not equal to answer
Prompt the user to input a guess, stored in the variable input
Format the input as an integer
If the guess is less than zero or greater than 100, print invalid input error
Else if the guess is less than the answer, print that the answer was too low
    and increment guesses by 1
Else print that the guess was too high and increment guesses by 1
End while
Print the number of guesses it took to get the answer

'''

from random import randint
from random import seed

seed(1)

generatedCorrectAnswer = randint(1, 100)
guessNumber = 1
print("Welcome to the Higher/Lower guessing game\n" +
                  "A number from 0 to 100 has been scretly generated.\n" +
                  "It is your task to guess what it is.\n" +
                  "How many guesses will it take you to find the right number?" +
                  "\n\n")
userInput = input("Guess {}: Enter a number between 0 and 100: ".format(guessNumber))

while int(userInput) != generatedCorrectAnswer:
    guessNumber += 1
    if int(userInput) > generatedCorrectAnswer:
        print("You guessed too high.  Please try again")
    else:
        print("You guessed too low.  Please try again")
    userInput = input("Guess {}: Enter a number between 0 and 100: ".format(guessNumber))

print("CORRECT!!!")
print("It took you {} guesses lto find the random number.\nThanks for playing".format(guessNumber))
