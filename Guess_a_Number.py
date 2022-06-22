import random
title = """  ________                                      _______               ___.                 
 /  _____/ __ __   ____   ______ ___________    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/\__  \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \\
\    \_\  \  |  /\  ___/ \___ \ \___ \  / __ \_/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >(____  /\____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/      \/         \/            \/    \/     \/       """
print(title)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")

answer = random.randint(1, 100)
print(answer)
level = input("Choose a difficulty level: 'easy' or 'hard': ")


def attempts():
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        return print("Invalid Entry.")


attempt = attempts()

guess = 0

while answer != guess:

    print(f"You have {attempt} attempts to guess the number.")

    guess = int(input("Make a guess: "))

    attempt = attempt-1

    if answer < guess:
        print("Too high.")
    elif answer > guess:
        print("Too low.")

    if answer == guess:
        print(f"You got it. The answer is {answer}.")

    print("Guess again.")
    if attempt == 0:
        print("You lose.")
        guess = answer
