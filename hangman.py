import random


def print_0_mistake():
    print(""" 
              |------|-
              |      |
              |      
              |     
              |      
             /|\\   
             /|\\

    """)


def print_1_mistake():
    print(""" 
              |------|-
              |      |
              |      o
              |     
              |      
             /|\\   
             /|\\

    """)


def print_2_mistake():
    print(""" 
              |------|-
              |      |
              |      o
              |      |
              |      |
             /|\\   
             /|\\

    """)


def print_3_mistake():
    print(""" 
              |------|-
              |      |
              |      o
              |     /|
              |      |
             /|\\   
             /|\\

    """)


def print_4_mistake():
    print(""" 
              |------|-
              |      |
              |      o
              |     /|\\
              |      |
             /|\\     |
             /|\\

    """)


def print_5_mistake():
    print(""" 
              |------|-
              |      |
              |      o
              |     /|\\
              |      |
             /|\\    /|
             /|\\

    """)


def print_6_mistake():
    print(""" 
              |------|-
              |      |
              |      o
              |     /|\\
              |      |
             /|\\    /|\\
             /|\\

    """)


def print_game_status():
    if mistake == 0:
        print_0_mistake()
    if mistake == 1:
        print_1_mistake()
    if mistake == 2:
        print_2_mistake()
    if mistake == 3:
        print_3_mistake()
    if mistake == 4:
        print_4_mistake()
    if mistake == 5:
        print_5_mistake()
    if mistake == 6:
        print_6_mistake()

    print('Word:', end='')
    for elements in guesses:
        print(f'{elements}', end='')
    print(f'\nyou have {remaining_guesses} guess(es) left')


words = ['absurd', 'boxful', 'crypt', 'duplex', 'exodus', 'funny', 'galaxy', 'hyphen', 'ivory', 'jackpot',
         'khaki', 'lucky', 'matrix', 'nightclub', 'oxygen', 'pajama', 'quiz']
guesses = []
remaining_guesses = 6
mistake = 0

word_index = random.randint(0, len(words)-1)
word = words[word_index].upper()
print(word)


for i in range(len(word)):
    guesses.append('_')

game_over = False
while not game_over:
    print_game_status()

    user_input = input('Please enter a letter:\n')

    if not user_input:
        print("That's not a valid input, Please try again")
    else:
        letter = user_input[0].upper()
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guesses[i] = letter
            if '_' not in guesses:
                game_over = True
        else:
            print('sorry, isn\'t of word')
            remaining_guesses -= 1
            mistake += 1
            if mistake == 6:
                game_over = True

if mistake == 6:
    print(print_game_status())
    print(f'sorry you lost, The word is {word}')
else:
    for i in range(4):
        print(" \U0001F389 \U0001F38A \U0001F388", end='')
    print()
    print('Congratulations, you won')
    print(f'The word is {word}')
