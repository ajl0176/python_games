import random

random_number = random.randint(1,10)
counter = 0

while counter < 8:
    counter +=1
    guess = int (input('What number would you like to guess:'))
    if guess < random_number:
        print ('Your guess is too low!')
    elif guess > random_number:
        print ('Your guess is too high!')
    elif guess == random_number:
        print ('Congrats!!')
    break

    if counter == 5:
        print('Sorry. You lose. The number was', random_number)
