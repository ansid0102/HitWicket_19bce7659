import pygame 
from chess.constants import *
from chess.pawn import Pawn
class Board:
    def __init__(self):
        self.board=[]
        self.selected_piece = None
        self.create_board()

    def draw_cubes(self,win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row%2,ROWS,2):
                pygame.draw.rect(win,WHITE,(row*SQUARE_SIZE,col*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col%2== ((row+1)%2):
                    if row<1:
                        self.board[row].append(Pawn(row,col,WHITE))
                    elif row>3:
                        self.board[row].append(Pawn(row,col,RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
                
    def draw(self,win):
        self.draw_cubes(win)
        for row in range(ROWS):
            for col in range(COLS):
                pawn = self.board[row][col]
                if pawn !=0:
                    pawn.draw(win) 
