#from os import readlink
import os
from image_to_ascii import ImageToAscii
#auxiliar functions for the format of color ANSI
from termcolor import cprint
#pure Python implementation of the http://www.figlet.org
from pyfiglet import FontError, figlet_format
#random functions
import random
#operations with regular expressions
import re

#functions of the game's image in ASCII code
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
    #clear the screen
    os.system('clear')
    #print in yellow color the message
    print_yellow = lambda x: cprint(figlet_format(x, font='avatar'),'yellow', attrs=['bold'])
    print_yellow('Hangman Game')



def run():
    lives = 3
    oportunities = 7

    while lives > 0:
        #clear the screen
        refresh()
        #begin_game(letter)
        #list of words of the file data.txt
        words = []
        #function for read of file data.txt with the game's words
        with open('./archivos/data.txt', 'r', encoding='utf-8') as f:
            for line in f:
                #read the line of the file removing the character line feed LF
                words.append(line.removesuffix(chr(10)))
            
        #dictionary with words groupeds for size
        dict_words = {
        j:[words[i] for i in range(170) if len(words[i]) == j ] for j in range(3,13) 
        }
        
        #calculate a random number for size of the word from 3 to 12
        #create a list with size of words
        size = [i for i in range(3,13)]
        #generate a random number for choice of size of the word
        random_size = random.choice(size)
        
        #get the list of words to find
        words_to_find = dict_words.get(random_size)
        words_to_find = list(enumerate(words_to_find))
        
        
        #generate a random number for the index of the element to find in the list choiced
        #for the random size
        random_index = random.randint(0,len(words_to_find)-1)


        #get the word to show
        word_game = words_to_find[random_index][1]

        #generate the track for the game
        track = ['_'] * random_size
        

        while oportunities >= 0:
            #clear the screen
            refresh()
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
                lives -= 1
                end_image()
                break
            print(word_game)
            
            #print the track        
            print(''.join(track))

            #validate if the word of game is complete
            complete = track.count('_')
            if complete == 0:
                break

            #read the letter
            letter = input('Enter a letter: ')

            #validate if the letter is in the word of the game
            ocurrencies = word_game.count(letter)
            if ocurrencies == 0:
                oportunities -= 1
            else:
                #with the functions of regular expressions we find all ocurrences of the letter 
                #in the word of game
                for character in re.finditer(letter, word_game, re.IGNORECASE):
                    track[character.start()] = character.group()


if __name__ == '__main__':
    run()