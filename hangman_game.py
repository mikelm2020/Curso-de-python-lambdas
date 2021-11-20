# From os import
import os
# Random functions
import random
# Operations with regular expressions
import re
# For obtain a delay
import time

from image_to_ascii import ImageToAscii
# Auxiliar functions for the format of color ANSI
from termcolor import cprint
# Pure Python implementation of the http://www.figlet.org
from pyfiglet import FontError, figlet_format


# Functions of the game's image in ASCII code
def start_image():
    print('+ - - - - +')
    print('|         |')
    for i in range(1,6):
        print('|          ')
    print('= = = = = =')


def fail1_image():
    print('+ - - - - +')
    print('|         |')
    print('|         0')
    for i in range(1,5):
        print('|          ')
    print('= = = = = =')
    

def fail2_image():
    print('+ - - - - +')
    print('|         |')
    print('|         0')
    print('|         |')
    for i in range(1,4):
        print('|          ')
    print('= = = = = =')


def fail3_image():
    print('+ - - - - +')
    print('|         |')
    print('|         0')
    print('|        /|')
    for i in range(1,4):
        print('|          ')
    print('= = = = = =')


def fail4_image():
    print('+ - - - - +')
    print('|         |')
    print('|         0')
    print('|        /|' + chr(92))
    for i in range(1,4):
        print('|          ')
    print('= = = = = =')


def fail5_image():
    print('+ - - - - +')
    print('|         |')
    print('|         0')
    print('|        /|' + chr(92))
    print('|        /')
    for i in range(1,3):
        print('|          ')
    print('= = = = = =')


def fail6_image():
    print('+ - - - - +')
    print('|         |')
    print('|         0')
    print('|        /|' + chr(92))
    print('|        / ' + chr(92))
    for i in range(1,3):
        print('|          ')
    print('= = = = = =')


def end_image():
    print('+ - - - - +')
    print('|         |')
    print('|          0')
    print('|        /|' + chr(92))
    print('|        / ' + chr(92))
    for i in range(1,3):
        print('|          ')
    print('= = = = = =')
    

def refresh():
    # Clear the screen
    os.system('clear')

def score(fails):
    points = 0
    if fails <= 1 and fails >= 0:
        points = 30
    elif fails <= 4 and fails >= 2:
        points = 20
    elif fails <= 6 and fails >= 5:
        points = 10
    elif fails == 7:
        points = -20
    
    return points


def run():
    lives = 3
    oportunities = 7
    fails = 0
    score_value = 0
    num_words = 0
    word_game = ''
   

    
    # List of words of the file data.txt
    words = []
    try:

        # Function for read of file data.txt with the game's words
        with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
            for line in f:
                # Read the line of the file removing the character line feed LF
                words.append(line.removesuffix(chr(10)))
        

        while lives >= 0:

            if oportunities == 0:
                lives -= 1
                if lives == 0:
                    oportunities = 0
                    fails = 7
                    # Print in red color the message
                    print_red = lambda x: cprint(figlet_format(x, font='avatar'),'red', attrs=['bold'])
                    print_red('Game Over')
                    break
                else:
                    oportunities = 7
                    fails = 0
                    # Print the word of the game 
                    print('😥 😥' , 'La palabra era: ' , word_game)
                    # Print in yellow color the message
                    print_yellow = lambda x: cprint(figlet_format(x, font='avatar'),'yellow', attrs=['bold'])
                    print_yellow('Try again')
                # Delay for  show the image of hanged man
                time.sleep(2)
                    
                

            # Generate the string of emojies lives
            string_lives = '💓 ' * lives

            # Dictionary with words groupeds for size
            dict_words = {
            j:[words[i] for i in range(170) if len(words[i]) == j ] for j in range(3,13) 
            }
            
            # Calculate a random number for size of the word from 3 to 12
            # Create a list with size of words
            size = [i for i in range(3,13)]
            # Generate a random number for choice of size of the word
            random_size = random.choice(size)
            
            # Get the list of words to find
            words_to_find = dict_words.get(random_size,list())
            words_to_find = list(enumerate(words_to_find))
            
            
            # Generate a random number for the index of the element to find in the list choiced
            # for the random size
            random_index = random.randint(0,len(words_to_find)-1)


            # Get the word to show
            word_game = words_to_find[random_index][1]
            # Convert the word to upper word
            word_game = word_game.upper()

            # Generate the track for the game
            track = ['_'] * random_size
            

            while oportunities >= 0:
                # Generate the string of oportunities
                string_oportunities = '😃 ' * oportunities
                # Clear the screen
                refresh()
                # Print in yellow color the message
                print_yellow = lambda x: cprint(figlet_format(x, font='avatar'),'yellow', attrs=['bold'])
                print_yellow('Hangman Game')
                print('Fails: ' , fails, '{:>40}'.format('Lifes: '), string_lives)
                print('Score: ', score_value, '{:>40}'.format('Oportunities: '), string_oportunities)
                print('Words: ', num_words)
                print(chr(13))

                if oportunities == 7:
                    start_image()
                elif oportunities == 6:
                    fail1_image()
                elif oportunities == 5:
                    fail2_image()
                elif oportunities == 4:
                    fail3_image()
                elif oportunities == 3:
                    fail4_image()
                elif oportunities == 2:
                    fail5_image()
                elif oportunities == 1:
                    fail6_image()
                elif oportunities == 0:
                    end_image()
                    break
                
                
                # Print the track        
                print(''.join(track))

                # Validate if the word of game is complete
                missing_letters = track.count('_')
                if missing_letters == 0:
                    score_value = score_value + score(fails)
                    oportunities = 7
                    fails = 0
                    num_words += 1
                    break


                try:
                    # Read the letter
                    letter = input('Enter a letter: ')
                    if not letter.isalpha():
                        raise NameError
                    # Validate if the letter is in lower case
                    if letter.islower():
                        # Convert to upper case
                        letter = letter.upper()
                    # Validate if the letter is in the word of the game
                    ocurrencies = word_game.count(letter)
                    if ocurrencies == 0:
                        oportunities -= 1
                        fails += 1
                        

                    else:
                        # With the functions of regular expressions we find all ocurrences of the letter 
                        # in the word of game
                        for character in re.finditer(letter, word_game, re.IGNORECASE):
                            track[character.start()] = character.group()
                except NameError:
                    print ('Please only a letter')

    except FileNotFoundError:
        print('No such file or directory /archivos/data.txt')

if __name__ == '__main__':
    run()