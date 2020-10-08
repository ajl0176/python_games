import random

user_number = int(input('Enter a number between 1 and 100:'))

count = 0
guess = 0

while guess != user_number:
    guess = random.randint(1,100)
    count +=1

print ('Computer guessed in', count, 'tries.')
