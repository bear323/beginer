import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("Too low guess again ")
        elif guess > random_number:
            print("Too high guess again ")
    
    print(f"You win you guessed the number {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback=""
    while feedback!="c":
        guess = random.randint(low,high)
        feedback = input(f"Is the {guess} too high h too low l or correct c : ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback=="l":
            low = guess + 1
    print("Horray!!!  :)")

        
computer_guess(100)