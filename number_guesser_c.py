import random

number = random.randint(1, 100)
guess = -1
count = 0

lower = 1
higher = 100

while guess != number:
    guess = int(input("Take a guess: "))
    count += 1
    if guess > number:
        print("Lower!\n")
    elif guess < number:
        print("Higher!\n")
    else:
        break
    cg = random.randint(lower, higher)
    print("The computer guessed: " + str(cg))
    count += 1
    if cg > number:
        higher = cg - 1
        print("Too high Computer.\n")
    elif cg < number:
        lower = cg + 1
        print("Too low Computer.\n")
    else:
        break
