import json
import random

FONT_COLORS = {'GREEN': '\033[92m',
           'YELLOW': '\033[93m',
           'RED': '\033[91m',
           'BLUE': '\033[94m',
           'CYAN': '\033[96m',
           'ENDC': '\033[0m',
           'BOLD': '\033[1m',
           'UNDERLINE': '\033[4m'}

QWERTY = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
          ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ' '],
          ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ', ' ', ' ']]

class Game():
    def __init__(self):
        with open ('five_letter_words.json', 'r') as f:
            self.dictionary = json.load(f)
        self.word = self.set_answer_word()
        self.guesses = []
        self.letters_guessed = {}
        
    def set_answer_word(self):
        # pick a random word from the words keys
        word = random.choice(list(self.dictionary.keys()))
        return word
    
    def get_answer_word(self):
        return self.word
    
    def make_guess(self, guess):
        # check if the guess is correct
        self.guesses.append(guess)
        self.add_letters_guessed(guess)
        if guess == self.word:
            return True
        else:
            return False

    def print_board(self):
        print('-' * 50)
        for i in range(6):
            print('|', end='')
            print(' ' * 4, end='')
            for j in range(5):
                to_print = '_'
                if i < len(self.guesses):
                    letter = self.guesses[i][j]
                    if letter == self.word[j]:
                        to_print = f'{FONT_COLORS["UNDERLINE"]}{FONT_COLORS["BOLD"]}{FONT_COLORS["GREEN"]}{letter}{FONT_COLORS["ENDC"]}'
                    elif letter in self.word:
                        to_print = f'{FONT_COLORS["UNDERLINE"]}{FONT_COLORS["YELLOW"]}{letter}{FONT_COLORS["ENDC"]}'
                    else:
                        to_print = f'{FONT_COLORS["UNDERLINE"]}{FONT_COLORS["RED"]}{letter}{FONT_COLORS["ENDC"]}'
                print(f'{FONT_COLORS["CYAN"]}{to_print}{FONT_COLORS["ENDC"]}', end=' ')
            
            # print a keyboard in the command line
            print(' ' * 10, end=' ')
            if i < len(QWERTY):
                for letter in QWERTY[i]:
                    if letter.lower() in self.letters_guessed:
                        print(f'{self.letters_guessed[letter.lower()]}{letter}{FONT_COLORS["ENDC"]}', end=' ')
                    else:
                        print(f'{FONT_COLORS["CYAN"]}{letter}{FONT_COLORS["ENDC"]}', end=' ')
                print(' ' * 3, end='|')
            else:
                print(' ' * 23, end='|')
            print('\n')

        print('-' * 50)

    def get_number_of_guesses(self):
        return len(self.guesses)

    def add_letters_guessed(self, guess):
        for i, letter in enumerate(guess):
            color = 'BLUE'
            if letter == self.word[i]:
                color = 'GREEN'
            elif letter in self.word:
                color = 'YELLOW'
            else:
                color = 'RED'
            self.letters_guessed[letter] = FONT_COLORS[color]