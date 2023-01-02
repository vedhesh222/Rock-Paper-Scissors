#Importing the Modules
from art import *
import random as r
import time as t

#Giving the Values
types = ['Rock', 'Paper', 'Scissor']


#Working with Art
print('+-------------------------------------------+')
print('             Rock Paper Scissors             ')
print('+-------------------------------------------+')
tprint("RPS",font = "isometric1")
print('.............................................')
print()

#Working with Game
s = input("Hit 'Enter' to Start ")
print()

print('Hey am Vedhesh :)')
print()

player = input("What's your Name: ")
print()

print('Cool', player, "can we play 'Rock Paper Scissors'")
print()

p = input("Enter 'Yes' to play: ")
print()
print('.............................................')
print()

if p == 'Yes':
    while True:
        t.sleep(1)
        print("Let's ")
        t.sleep(0.3)
        print('Go...')
        t.sleep(2)
        print()
        break

    while True:
        i = input('Rock, Paper, Scissor or Quit: ')
        print()

        ran = r.randint(0,2)
        bot = types[ran]
        
        print('Vedhesh:',bot)
        print()
        t.sleep(1)

        if i == 'Rock':
            if bot == 'Rock':
                print('Vedhesh: Cool tough Competitor!')
                print()
                print('.............................................')
                print()
                
            elif bot == 'Scissor':
                print('Vedhesh: Oops, You have Won!')
                print()
                print('.............................................')
                print()
                
            elif bot == 'Paper':
                print('Vedhesh: Yes, I have Won!')
                print()
                print('.............................................')
                print()
                
        elif i == 'Paper':
            if bot == 'Rock':
                print('Vedhesh: Oops, You have Won!')
                print()
                print('.............................................')
                print()
                
            elif bot == 'Scissor':
                print('Vedhesh: Yes, I have Won!')
                print()
                print('.............................................')
                print()
                
            elif bot == 'Paper':
                print('Vedhesh: Cool tough Competitor!')
                print()
                print('.............................................')
                print()

        elif i == 'Scissor':
            if bot == 'Rock':
                print('Vedhesh: Yes, I have Won!')
                print()
                print('.............................................')
                print()
                
            elif bot == 'Scissor':
                print('Vedhesh: Cool tough Competitor!')
                print()
                print('.............................................')
                print()
                
            elif bot == 'Paper':
                print('Vedhesh: Oops, You have Won!')
                print()
                print('.............................................')
                print()
	
        elif i == 'Quit':
            print('Losser :)')
            t.sleep(1)
            break

        else:
            print("Vedhesh: Bro what's this")
            print()
            print('.............................................')
            print()
                
else:
    while True:
        print("B", end='')
        t.sleep(0.1)
        print('y', end='')
        t.sleep(0.1)
        print('e', end='')
        t.sleep(0.1)
        print(" ", end='')
        t.sleep(0.1)
        print(":", end='')
        t.sleep(0.1)
        print('(', end='')
        print()
        break


