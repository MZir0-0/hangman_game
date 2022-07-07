import random
import string
import sys


print(f'H A N G M A N')
wins = 0
loses = 0

def play():
    random_word = random.choice(['python', 'java', 'swift', 'javascript'])
    hiden_word = len(random_word) * '-'
    guessed_letters = set()
    attempts = 8
    while attempts > 0:
        print()
        print(hiden_word)
        letter = input('Input a letter: ')
        
        if len(letter) != 1:
            print('Please, input a single letter.')
            continue
        elif letter not in string.ascii_lowercase:
            print('Please, enter a lowercase letter from the English alphabet.')
            continue
        elif letter in hiden_word or letter in guessed_letters:
            print('You\'ve already guessed this letter.')
            continue
        else:
            if letter in random_word:
                guessed_letters.add(letter)
                for i in range(0, len(random_word)):
                    if letter == random_word[i]:
                        hiden_word = hiden_word[:i] + letter + hiden_word[i+1:]  
            else:
                guessed_letters.add(letter)
                print('That letter doesn\'t appear in the word.')
                attempts -= 1
                continue
        
        if hiden_word == random_word:
            print(f"You guessed the word {hiden_word}!\nYou survived!")
            global wins
            wins += 1
            break

    if hiden_word != random_word:
        global loses
        loses += 1
        print('You lost!')
    
        
def result():
    return print(f'You won: {wins} times.\nYou lost: {loses} times.')
    

while True:
    inp = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if inp == 'play':
        play()
    elif inp == 'results':
        result() 
    elif inp == 'exit':
        break

