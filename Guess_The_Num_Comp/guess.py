import random


def guess(x):
    random_number = random.randint(1, x)
    guess_usr = 0
    while guess_usr != random_number:
        guess_usr = int(input(f"Guess a number between 1 and {x} : "))
        if guess_usr < random_number:
            print("Sorry, guess again. Too low")
        elif guess_usr > random_number:
            print("Sorry, guess again. Too high")
    print(f"Yay! you have guessed the number {random_number} Correctly")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess_comp = random.randint(low, high)
        else:
            guess_comp = low
        feedback = input(f"Is {guess_comp} too high (H), too low (L), or correct(C) -> ").lower()
        if feedback == 'h':
            high = guess_comp - 1
        elif feedback == 'l':
            low = guess_comp + 1
    print(f"Yay! the computer guessed your number {guess_comp}, correctly")


computer_guess(1000)
