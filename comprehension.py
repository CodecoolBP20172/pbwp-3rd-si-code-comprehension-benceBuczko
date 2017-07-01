import random
# You have 6 chances to guess the number randomly generated between 1 and 20.
guessesTaken = 0  # Assigns 0 to guessesTaken

print('Hello! What is your name?')  # Prints to the console 'Hello! What is your name?'
myName = input()  # Asks the user for inout and assigns it to myName

number = random.randint(1, 20)  # Generates a random number between 1 and 20 (including both ends) and assigns it to number 
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Prints 'Well, ' + myName + ', I am thinking of a number between 1 and 20.'

while guessesTaken < 6:  # Does the following until guessesTaken reaches 6
    print('Take a guess.')  # Prints 'Take a guess.'
    guess = input()  # Asks the user for inout and assigns it to guess
    guess = int(guess)  # Converts guess to an integer

    guessesTaken += 1  # Increases guessesTaken by 1

    if guess < number:  # Checks if guess is lower than number
        print('Your guess is too low.')  # Prints 'Your guess is too low.'

    if guess > number:  # Checks if guess is higher than number
        print('Your guess is too high.')  # Prints 'Your guess is too high.'

    if guess == number:  # Checks if guess equals number
        break  # Breaks the loop

if guess == number:  # Checks if guess equals number (again?, not dry...)
    guessesTaken = str(guessesTaken)  # Converts guessesTaken to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Prints 'Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!'

if guess != number:  # Checks if guess does not equal number
    number = str(number)  # Converts number to a string
    print('Nope. The number I was thinking of was ' + number)  # Prints 'Nope. The number I was thinking of was ' + number
