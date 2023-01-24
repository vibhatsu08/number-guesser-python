# All the "hints given by the computer" will be enclosed between "... ..."
# Any statements asking for "input" will begin with a "---> " and end with a " : "
# Any other statements, "stating the obvious" will begin with a "-> "
# The running program statement will be enclosed between "### ###"

# The random module to import the random function.
import random
# importing the time module, to add a certain time delay for some flair.
import time

# Starts the game with the input response.
def startGame () :
    # Asks for input, yes or no.
    response = input("---> Do you want to play the number guesser game...Enter yes or no to get started : ")
    # If the reponse from the user is yes.
    if response.lower() == "yes" :
        timeDelay ()
        print("-> Response was : yes")
        runningProgramStatement ()
        chooseNumber ()
        
    # If the response from the user is no.
    elif response.lower() == "no" :
        return "-> See you the next time!"
    
    else :
        startGame ()
    
    return "-> Thank you for playing!, See you next Time!"

# Function for the computer to choose the number
def chooseNumber () :
    print("-> The Computer has chosen the number...")
    numberChosen = random.randint(0, 100)
    timeDelay ()
    runningProgramStatement ()
    initializeGame (numberChosen)

def initializeGame (numberChosen) :
    # TBD - convert these print statements into an array of strings to be looped and printed.
    timeDelay ()
    print("-> Your task is to guess the number chosen by the computer...")
    timeDelay ()
    print("-> You will be provided with 10 tries...")
    timeDelay ()
    print("-> With every unsuccessful attempt, the computer will provide a hint to you...")
    timeDelay ()
    print("-> Good luck!")
    
    # Number of attempts for the user, starts at 0, will keep incrementing by 1.
    attempts = 0
    runningProgramStatement ()
    print("---> Guess your number : ")
    guessNumberGame (attempts, numberChosen)
    timeDelay ()
    
# Function to guess the number chosen by the computer
def guessNumberGame (attempts, numberChosen) :
    guessNumber = int(input())
    if guessNumber > 100 or guessNumber < 0 :
        timeDelay ()
        print("...C'mon, be realistic, you need to choose a number between 0 and 100...")
        attempts += 1
        guessNumberGame (attempts, numberChosen)
    if guessNumber > numberChosen :
        timeDelay ()
        print("...Try lower...")
        attempts += 1
        guessNumberGame (attempts, numberChosen)
    if guessNumber < numberChosen :
        timeDelay ()
        print("...Try higher...")
        attempts += 1
        guessNumberGame (attempts, numberChosen)
        
    if guessNumber == numberChosen :
        timeDelay ()
        gameOver (attempts, numberChosen)

# Function for the final part of the game.
def gameOver (attempts, numberChosen) :
    print("-> AWESOME, you've correctly guessed the number, it took you {} tries to get to the correct answer!".format(attempts))
    return ""
            
# Function for the running program statement
def runningProgramStatement () :
    print("### RUNNING PROGRAM ###")
    timeDelay ()
    
def timeDelay () :
    time.sleep(2)
    
# Takes the input response.
print(startGame ())