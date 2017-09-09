'''
Created on 09.09.2017

@author: Tibu
'''

import numpy
from de.mathis.InvalidMoveException import InvalidMoveException


board = numpy.array([[-1, -1, 1, 1, 1, -1, -1]
                       , [-1, -1, 1, 1, 1, -1, -1]
                        , [1, 1, 1, 1, 1, 1, 1]
                        , [1, 1, 1, 0, 1, 1, 1]
                        , [1, 1, 1, 1, 1, 1, 1]
                        , [-1, -1, 1, 1, 1, -1, -1]
                        , [-1, -1, 1, 1, 1, -1, -1]]
                        , numpy.int32)

labels = {-1:' ', 0:'\u00B7', 1:'x'}

class SolitaireBoard():
    
    def _getSymbolForValue(self, value):
        return labels[value]
    
    def printBoard(self):
        print('+' + '-' * 15 + '+')
        for row in range(len(board)):
            print('| ' + ' '.join(self._getSymbolForValue(board[row][p]) for p in range(len(board[row]))) + ' |') 
        print('+' + '-' * 15 + '+')
        
    def printBoardAndIndices(self):
        print('+' + '-' * 15 + '+' + ' ' + '+' + '-' * 22 + '+') 
        for row in range(len(board)):
            rowLen=len(board[row])
            print('| ' + ' '.join(self._getSymbolForValue(board[row][cell]) for cell in range(rowLen)) + ' |' 
                  + ' '
                + '| ' + ' '.join('{:>2}'.format( ' ' if self._getValueOfField(row*rowLen+cell) < 0 else str(row*rowLen+cell)) for cell in range(rowLen)) + ' |')
        print('+' + '-' * 15 + '+' + ' ' + '+' + '-' * 22 + '+') 
        
    def printIndices(self):
        print('+' + '-' * 22 + '+')
        for i in range(7):
            print('| ' + ' '.join('{:>2}'.format(str(i*7+j)) for j in range(7)) + ' |') 
        print('+' + '-' * 22 + '+')

    def _indexToRow(self, index):
        row = int(index / 7)  
        return row
    
    def _indexToCell(self, index):
        cell = int(index % 7)
        return cell

    def _getValueOfField(self, index):
        return board[self._indexToRow(index)][self._indexToCell(index)]

    def getField(self, index):
        return self._getSymbolForValue(self._getValueOfField(index))

    def moveAndPrint(self,current, target):
        self.move(current, target)
        self.printBoardAndIndices()
        
    def move(self, current, target):
        print('Moving {} to {}...'.format(current, target))
        
        rowA = self._indexToRow(current)
        rowB = self._indexToRow(target)
        colA = self._indexToCell(current)
        colB = self._indexToCell(target)

        if rowA != rowB and colA != colB:
            raise InvalidMoveException("Cant move diagonal (from {} to {})".format(current, target))
        
        horizontalMove = rowA == rowB
        
        distance = abs(colA- colB) if horizontalMove else abs(rowA- rowB)
        currentField = board[rowA][colA]
        targetField = board[rowB][colB]
        
        betweenIndex = -1
        
        if horizontalMove:
            betweenIndex = current - 1 if colA > colB else target - 1
        else:
            betweenIndex = current - 7 if rowA > rowB else target - 7
                
        betweenField = self._getValueOfField(betweenIndex)

        if distance != 2 :
            raise InvalidMoveException('illegal move: from {} to {}'.format(current, target))
        if currentField != 1 :
            raise InvalidMoveException('no stone at current {} (found {} instead)'.format(current, self._getSymbolForValue(currentField)))
        if(targetField != 0):
            raise InvalidMoveException('no empty field at targetField {}  (found {} instead)'.format(target, self._getSymbolForValue(targetField)))
        if(betweenField != 1):
            raise InvalidMoveException('cant jump over {}'.format(self._getSymbolForValue(betweenField)))
        
        board[self._indexToRow(betweenIndex)][self._indexToCell(betweenIndex)] = 0
        board[rowB][colB] = 1
        board[rowA][colA] = 0
        
        