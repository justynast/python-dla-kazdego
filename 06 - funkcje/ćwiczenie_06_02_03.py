"""
2. Zmodyfikuj projekt 'Jaka to liczba?' z rozdziału 3. przez użycie w nim funkcji ask_number().
3. Zmodyfikuj nową wersję gry 'Jaka to liczba?', którą utworzyłeś w ramach poprzedniego zadania, tak
aby kod programu znalazł się w funkcji o nazwie main().
"""

import random

def displayInstruction():
    """ display instruction of the game """
    print(
    """
    Hello human!
    I am thinking about a number between 1 and 100.
    Try to guess the number!
    """
    )

def getNumber():
    """ generate random number in range 1-100 """
    theNumber = random.randint(1, 100)
    return(theNumber)

def askNumber(question, low, high):
    """ ask about the number in range """
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def prompt(theNumber, guess):
    """ display prompt """
    if guess > theNumber:
        print("Your guess is too big.")
    elif guess < theNumber:
        print("Your guess is too small.")

def winning(theNumber, guess):
    """ determine winning condition """
    if theNumber == guess:
        return True

def congrat(theNumber, tries):
    """ congratulate player and display the number of tries"""
    print("Yes, the number I'm thiking of is", theNumber)
    print("It took you", tries, "tries to guess. Congratulations!")



def main():
    theNumber = getNumber()
    displayInstruction()
    guess = askNumber("What number am I thinking about? ", 1, 100)
    tries = 1
    while not winning(theNumber, guess):
        prompt(theNumber, guess)
        guess = askNumber("\nWhat number am I thinking about? ", 1, 100)
        tries += 1

    congrat(theNumber, tries)

main()
input("\n\nPress any key to exit")
