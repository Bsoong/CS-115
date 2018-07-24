'''
Created on Dec 4, 2017

@author: brandon
I pledge my Honor that I have abided by the Stevens Honor System -- Bsoong
'''

class Board(object):
    def __init__(self, width= 7, height = 6):
        """Creates the row"""
        self.__width = width
        self.__height = height
        self.__board = []
        for x in range(self.__height):
            self.__board += [[' '] * self.__width]
            
    
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @width.setter
    def width(self, width=7):
        self.__width = width
    @height.setter
    def height(self, height = 6):
        self.__height = height
            
        
    
    def __str__(self):
        """Creates the board"""
        board = []
        s = ""
        for x in range(len(self.__board)):
            s += '\n |'
            for i in range(len(self.__board[x])):
                s += self.__board[x][i] + "|"
        s += '\n ' + '-' * (self.__width *2 +1)
        hold = ''
        for n in range(self.__width):
            hold += " " + str(n)
        s += '\n' + ' ' + hold
        return s
                
    def allowsMove(self, col):
        """Checks if a move is viable"""
        if int(col) < 0 or int(col) > self.__width-1:
            return False
        else:
            for i in range(self.__height):
                if self.__board[(self.__height -1)- i][int(col)] == ' ':
                    return True
            return False
    def addMove(self, col, ox):
        """Adds a move"""
        if int(col) > self.__width - 1 or int(col) < 0: 
            print("Please choose a row in the board")
        else: 
             for x in range(self.__height):
                if self.__board[self.__height-1 - x][int(col)] == ' ':
                    self.__board[self.__height - 1 - x][int(col)] = ox
                    break
   
        
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'. For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the bottom row, or b.setBoard('000000') to
        see them alternate in the left column. 
        moveString must be a string of integers     
        """
        nextCh = 'X' 
        for colString in moveString:
            col = int(colString)
            if 0<= col <= self.__width:
                self.__addMove(col, nextCh)
            if nextCh == 'X': 
                nextCh = 'O'
            else:
                nextCh = 'X'
    def delMove(self, col):
        """Deletes a move"""
        for x in range(self.__height):
            if self.__board[x][int(col)] != ' ':
                 self.__board[x][int(col)] = ' '
                 break
        
    def winsFor(self, ox):
        """Searches for the potential ways to win"""
        count = 0
        for x in range(self.__height-3):
            for y in range(self.__width):
                for i in range(4):
                    if self.__board[x+i][y] == ox:
                        count +=1
                    if count == 4:
                        return True
                count = 0
        for x in range(self.__height-3):
            for y in range(self.__width-3):
                for i in range(4):
                    if self.__board[x+i][y+i] == ox:
                        count +=1
                    if count == 4:
                        return True
                count = 0
        for x in range(self.__height):
            for y in range(self.__width-3):
                for i in range(4):
                    if self.__board[x][y+i] == ox:
                        count +=1
                    if count == 4:
                        return True
                count = 0
        for x in range(self.__height):
            for y in range(self.__width-3):
                for i in range(4):
                    if self.__board[self.__height-1-(x+i)][y+i] == ox:
                        count +=1
                    if count == 4:
                        return True
                count = 0
        return False
                    
         
    def hostGame(self):
        """Creates a loop and runs the program"""
        print("Welcome to Connect Four!")
        var = 0
        W = False
        print(self)
        while W != True:
            if var == 0:
                temp = 0
                while temp == 0:
                    try:
                        input1 = int(input("X's choice: "))
                    except ValueError:
                        print("Please enter a valid input")
                        continue
                    if self.allowsMove(input1):
                            self.addMove(input1, 'X')
                            temp += 1
                    else: 
                        print("Please enter a valid input")
                W = self.winsFor('X')
                if W == True:
                    print("X wins -- Congratulations!")
                    print(self)
                    break
                ex = 0
                for i in range(self.__width):
                    if self.allowsMove(i):
                        ex +=1
                if ex == 0:
                    print("Game Over!")
                    print(self)
                    W = True
                    break
                var += 1
            else:
                temp = 0
                while temp == 0:
                    try:
                        input2 = int(input("O's choice: "))
                    except ValueError:
                        print("Please enter a valid input")
                        continue
                    if self.allowsMove(input2):
                            self.addMove(input2, 'O')
                            temp += 1
                    else: 
                        print("Please enter a valid input")
                W = self.winsFor('O')
                if W == True:
                    print("O wins -- Congratulations!")
                    print(self)
                    break
                ex = 0
                for i in range(self.__width):
                    if self.allowsMove(i):
                        ex +=1
                if ex == 0:
                    print("Game Over!")
                    print(self)
                    W = True
                    break
                var -= 1
            print(self)

if __name__ == '__main__':
    b = Board(7,6)
    b.hostGame()
   