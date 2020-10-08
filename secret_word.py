import random

with open ('usr/share/dict/words') as infile:
    words = infile.read()splitlines()

def start_game():
    #lower used b/c want all lower case letters
    random_word = random.choice(words).lower()
    char_list = list(rand_word)
    #len is for word length and _ is for each letter in the words
    display_list = ['_'] * len(random_word)

    print(f'There are {len(random_word)}) letters in your word.')

    remaining_guesses = 10
    guesses_made = []

    while remaining_guesses > 0:
        guess = input('Guess a letter: ').lower()

        if guess in guesses_made:
            print('Oops. Guess again.')
        else:
            guesses_made.append(guess)

            if guess in char_list:
                for index, char in enumerate(char_list):
                    if char == guess:
                        display_list[index] = guess
                if '_' not in display_list:
                    print('Congratulations! You\'re a winner!')
                    break
                else:
                    print('Great job! You\'ve guessed a letter')
                    print(''.join(display_list))
            else:
                remaining_guesses -= 1
                if remaining_guesses == 0:
                    print('You Lost!')
                else:
                    if remaining_guesses == 1:
                        guess_text = 'guess'
                    else:
                        guess_text = 'guesses'
                    print(f'Oops. That\'s a bad guess. You have {remaining_guesses} {guest_text}) letters left.')
                    print(''.join(display_list))
