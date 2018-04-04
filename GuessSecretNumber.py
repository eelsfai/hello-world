guess = 0
low = 1
userInput =1
high = 100
guess = (low + high)/2
print("Please think of a number between 0 and 100!")
while userInput != 'c':
    print("Is your secret number %s?" %str(guess))
    userInput =1
    while userInput!='h' and userInput!='l' and userInput!='c':
        userInput = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. \n")
        if userInput!='h' and userInput!='l' and userInput!='c':
            print("Sorry, I did not understand your input. \n")
            print("Is your secret number %s?" %str(guess))
    if userInput == 'h':
        high = guess
    elif userInput == 'l':
        low = guess
    else:
        break
    guess = (low+high)/2
print("Game over. Your secret number was: " + str(guess))
