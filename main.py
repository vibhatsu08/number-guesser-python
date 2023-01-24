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
    return "Thank you for playing!, See you next Time!"

# function for the computer to choose the number
def chooseNumber () :
    print("The Computer has chosen the number...")
    numberChosen = random.randint(0, 100)
    runningProgramStatement ()
    initializeGame (numberChosen)

def initializeGame (numberChosen) :
    # tbd - convert these print statements into an array of strings to be looped and printed.
    print("Your task is to guess the number chosen by the computer...")
    print("You will be provided with 10 tries...")
    print("With every unsuccessful attempt, the computer will provide a hint to you...")
    print("Good luck!")
    
    # number of attempts for the user, starts at 0, will keep incrementing by 1.
    attempts = 0
    runningProgramStatement ()
    print("...guess your number...")
    guessNumberGame (attempts, numberChosen)
    
# function to guess the number chosen by the computer
def guessNumberGame (attempts, numberChosen) :
    guessNumber = int(input())
    if guessNumber > 100 or guessNumber < 0 :
        print("...c'mon, be realistic, you need to choose a number between 0 and 100...")
        attempts += 1
        guessNumberGame (attempts, numberChosen)
    if guessNumber > numberChosen :
        print("...try lower...")
        attempts += 1
        guessNumberGame (attempts, numberChosen)
    if guessNumber < numberChosen :
        print("...try higher...")
        attempts += 1
        guessNumberGame (attempts, numberChosen)
        
    if guessNumber == numberChosen :
        gameOver (attempts, numberChosen)

# function for the final part of the game.
def gameOver (attempts, numberChosen) :
    print("---AWESOME, you've correctly guessed the number, it took you {} tries to get to the correct answer---".format(attempts))
    return ""
            
# function for the running program statement
def runningProgramStatement () :
    print("...RUNNING PROGRAM...")
    
# takes the input response.
print(startGame ())