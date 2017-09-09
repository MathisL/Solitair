'''
Created on 09.09.2017

@author: Mathis

'''
from de.mathis.SolitairBoard import SolitairBoard 

print('Hi! Welcome to this simple solitair game. Have fun and good luck! (press h for help, x to quit)')

board = SolitairBoard()
board.printBoardAndIndices()


def printHelp():
    print('sorry I have no idea how this works either')

while(True):
    print('Enter your move (stone and target separated by space):')
    read = input()
    if read.startswith('x'):
        break
    if read.startswith('h'):
        printHelp()
        continue
    split = read.split(sep=' ')
    try:
        a = int(split[0])
        b = int(split[1])
        board.moveAndPrint(a, b)
    except: 
        print('Invalid input')