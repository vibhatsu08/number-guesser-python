# Number guessing game

# import the random module, to help generate the random number between the provided limits.
import random

# welcome message
print("Welcome to the number guessing game!")
# enter yes or no to either get started with the game, or end the game.
print("Enter \"y\" or \"yes\" to get started or \"n\" or \"no\" to abort the program: ")

enterCode = int(input("y | yes or n | no : "))
if (enterCode.lower() == "yes" or enterCode.lower() == "y") :
    # lower limit, asks for the starting point of the range.
    lowerPoint = int(input("Enter the starting point for the range: "))
    # higher limit, asks for the ending point of the range.
    higherPoint = int(input("Enter the ending point for the range: "))
    
    # the computer chooses the random number : 
    numberChosen = random.randint(lowerPoint, higherPoint)
        
    print("To guess the number between {} and {}!".format(lowerPoint, higherPoint))
    
    # this will keep a track of the user's score through the game. Maximum tries is 8.
    scoreKeeper = 0
    # tries limit, maximum number of tries for the user.
    maximumAttempts = 8
    
    for i in range (1, maximumAttempts+1) :
        # this loop will run as long as the score keeper is less than 8.
        if scoreKeeper < 8:
            print("Guess a random number....")
            # takes the input for number by the user.
            guessedNumber = int(input("---> "))
            
            # if the guessed number is not equal to the chosen number and the maximum attempts are not equal to zero.
            if guessedNumber != numberChosen and maximumAttempts != 0 :
                # decrements the maximum attempts by the user, the user gets 8 chances to correctly guess the number.
                # if failed to do so, the maximumAttempt decrements by 1, and the score keeper increments by 1.
                maximumAttempts -= 1
                scoreKeeper += 1
                print("Hmmm, all right let me give you a little hint!")
                
                # first case, if the guessed number is in the upper half of the number, and the "number chosen" is also in the upper half of the number range.
                if ((numberChosen >= higherPoint//2) and  (guessedNumber >= higherPoint//2) and (guessedNumber <= higherPoint)) :
                    
                    
                
                
elif (enterCode.lower() == "no" or enterCode.lower() == "n") :
    print("See you the next time!")
else :
    print("Invalid answer!")