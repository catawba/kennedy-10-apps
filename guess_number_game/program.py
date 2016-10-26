import random

print('---------------------------------')
print('       Guess Number App')
print('---------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
name = input("Enter a name: ")

while guess != the_number:
    guess_text = input('Guess a number between 1 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print("Sorry {}, your guess of {} is too low".format(name, guess))
    elif guess > the_number:
        print("Sorry {}, your guess of {} is too high".format(name, guess))
    else:
        print("Excellent work {}, you won. It was {}!".format(name, guess))
