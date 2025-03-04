import random

number_to_guess = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100): "))
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("You got it!")
        break

