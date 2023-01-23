# the random module to import the random function.
import random

# starts the game with the input response.
def startGame () :
    response = input("Do you want to play the number guesser game...Enter yes or no to get started: ")
    if response.lower() == "yes" :
        print("response was : yes")
        runningProgramStatement ()
        chooseNumber ()
        
    elif response.lower() == "no" :
        return "See you the next time!"

# function for the computer to choose the number
def chooseNumber () :
    print("The Computer has chosen the number...")
    numberChosen = random.randint(0, 100)
    runningProgramStatement ()
    initializeGame (numberChosen)


def initializeGame (numberChosen) :
    print("Your task is to guess the number chosen by the computer...")
    print("You will be provided with 10 tries...")
    print("With every unsuccessful attempt, the computer will provide a hint to you...")
    print("Good luck!")
    
    attemptsLeft = 10
    runningProgramStatement ()
    guessNumberGame (attemptsLeft, numberChosen)
    
# function to guess the number chosen by the computer
def guessNumberGame (attemptsLeft, numberChosen) :
    while (attemptsLeft != 0) :
        guessNumber = int(input("---> Guess your number ---> "))
        if (guessNumber > 100//2) and (guessNumber != numberChosen) :
            # print("...choose a number between mid point of the range and till the end...")
            attemptsLeft -= 1
        if (guessNumber < numberChosen//2) and (guessNumber != numberChosen) :
            print("")
        if guessNumber == numberChosen :
            gameOver (attemptsLeft)

# function for the final part of the game.
def gameOver (attemptsLeft, numberChosen) :
    if attemptsLeft == 10 :
        print("...holy smokes, that was amazing, good job mate...")
    if attemptsLeft >= 7 and attemptsLeft < 10:
        print("...good job, you took less tries compared to your other attempts...")
    elif attemptsLeft >= 3 and attemptsLeft < 7 :
        print("...well done, see you next time, remember to make your judgement better, always \'USE THE FORCE!!!\'...")
    elif attemptsLeft > 0 and attemptsLeft < 3 :
        print("...good job, you finally did it, thanks for playing the complete run of the game, adios amigo...")
    elif attemptsLeft == 0 :
        print("...that was a surprising roller coster of events back there, anyways, the number chosen by the computer is {}, see you next time buddy...".format(numberChosen))
            
# function for the running program statement
def runningProgramStatement () :
    print("...RUNNING PROGRAM...")
# takes the input response.
print(startGame ())