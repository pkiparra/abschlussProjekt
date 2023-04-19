import sys
import numpy as np
import ctypes
import pygame
from pygame.locals import *
import math
import tkinter as regeln
import tkinter.font as tkFont



#Draw Board
def draw_board(board):
    for row in range(6):
        for col in range(6):
            if board[row][col] == 'X':
                screen.blit(p1_img, ((col * 100) + 15 , (row * 100) + 12))

            elif board[row][col] == 'O':
                screen.blit(p2_img, ((col * 100) + 11 , (row * 100) + 10))

#Check Winner
def check(boardlist, player, y, x):
        if player == 1:
            boardlist[y][x] = 'X'
            check_win_HV(boardlist, 'X')
        else:
            boardlist[y][x] = 'O'
            check_win_HV(boardlist, 'O')

#Check Winner
def check_win_HV(boardlist, element):
    arindex = []
    #Horizontal
    for i in range(6):
        for j in range(3):
            if (boardlist[i][j] == boardlist[i][j+1] == boardlist[i][j+2] == boardlist[i][j+3] == element):
                ind2 = [i,j]
                arindex.append(ind2)
                farbe(arindex, 1, element)
    #Vertikal
    for i in range(3):
        for j in range(6):            
            if (boardlist[i][j] == boardlist[i+1][j] == boardlist[i+2][j] == boardlist[i+3][j] == element):
                ind2 = [i,j]
                arindex.append(ind2)
                farbe(arindex, 2, element)   

    #Diagonal --->>>               
    for i in range(3):
        for j in range(3):
            # Check diagonal from top-left to bottom-right
            if (boardlist[i][j] == boardlist[i+1][j+1] == boardlist[i+2][j+2] == boardlist[i+3][j+3]) and boardlist[i][j] == element:
                ind2 = [i,j]
                arindex.append(ind2)
                farbe(arindex, 3, element)
                
            # Check diagonal from bottom-left to top-right
            if (boardlist[i+3][j] == boardlist[i+2][j+1] == boardlist[i+1][j+2] == boardlist[i][j+3]) and boardlist[i+3][j] == element:
                ind1 = [i+3,j]
                arindex.append(ind1) 
                farbe(arindex, 4, element)
                
#Gewonnene Reihe wird Farblich hinterlegt
def farbe(indexx, num, element):
    
    if num == 1:
        row = indexx[0][0] * 100
        col = indexx[0][1] * 100
        for i in range(4):
            x = i * 100
            pygame.draw.line(screen, 'white',  ((col + x) , (row +  50)), ((col + x + 100) , (row + 50)), 101)
    if num == 2:
        row = indexx[0][0] * 100
        col = indexx[0][1] * 100
        for i in range(4):
            x = i * 100
            pygame.draw.line(screen, 'white',  ((col + 100) , (row + x +  50)), ((col) , (row + x + 50)), 101)

    if num == 3:
        row = indexx[0][0] * 100
        col = indexx[0][1] * 100
        for i in range(4):
            x = i * 100
            pygame.draw.line(screen, 'white',  ((col + x) , (row + x + 50)), ((col + x + 100) , (row + x + 50)), 101)

    if num == 4:
        row = indexx[0][0] * 100
        col = indexx[0][1] * 100
        for i in range(4):
            x = i * 100
            pygame.draw.line(screen, 'white',  ((col + x) , (row - x + 50)), ((col + x + 100) , (row - x + 50)), 101)
    
    update_break(element)

def create_popup():    
    Font_tuple = ("Comic Sans MS", 10, "bold")
    
    popup = regeln.Label( text="Dieses Spiel wird in dieser Version ebenfalls auf einem \n "
                                "6x6 Spielfeld gespielt und ist auch unter dem Namen ,Vier \n"
                                "gewinnt´ bekannt. Beide Spieler setzen abwechselnd ihre \n"
                                "Spielsteine auf ein freies Feld. Der Spieler, der als Erster \n"
                                "vier seiner Spielsteine in eine Zeile, Spalte oder Diagonale \n"
                                "setzen kann, gewinnt. Das Spiel ist unentschieden, wenn alle \n"
                                "Felder belegt sind, ohne dass ein Spieler die erforderlichen \n"
                                "Spielsteine in einer Reihe, Spalte oder Diagonalen setzen konnte.", font = Font_tuple )
    
    popup.pack(pady=5)

    popup.mainloop()




#PopUp
def popup(element):
    messageBox = ctypes.windll.user32.MessageBoxW
    if element == 'end':
        a = 'Gamedraw : Niemand hat gewonnen'
    else:
        a = element + " hat gewonnen"

    returnValue = messageBox(None, a,"Game Over",0x70 | 0x0)


    if returnValue == 1:
        #Muss Hauptmenu ------>>>>>>>>>>>>>>>>>
        print("Game Over")
        pygame.quit()
        sys.exit()

#Update Screen and Break   
def update_break(element):
    draw_board(boardlist)
    pygame.display.update()
    finish(element)

#Game Ende Pop-Up
def finish(element):
    pygame.display.update()

# Checkt ob move Valide ist und gibt an welcher Spieler dran ist.
def validMove(boardlist,player,x,y):
    if boardlist[y][x] == '-':
        check(boardlist, player, y, x)
        if player == 1:
            player = 2
        else:
            player = 1
    return player



pygame.init()      
#Fenster Große
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Fenster erstellen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
bg_img = pygame.image.load('Images/BG_tic.png')
bg_img = pygame.transform.scale(bg_img,(SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Tic Tac Toe 6x6')

#Images
screen.blit(bg_img, (0, 0))
p1_img = pygame.image.load('Images/x_tic.png')
p1_img = pygame.transform.scale(p1_img, (75, 75))

p2_img = pygame.image.load('Images/O_tic.png')
p2_img = pygame.transform.scale(p2_img, (80, 80))

#Main Array
boardlist = np.array([
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-']])

player = 1
count_draw = 0
while True:
    draw_board(boardlist)
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    for event in pygame.event.get():

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                b = pygame.mouse.get_pos()
                x = int(b[0] / 100)
                y = int(b[1] / 100)
                player = validMove(boardlist, player, x, y)
                if count_draw == 36:
                    draw_board(boardlist)
                    pygame.display.update()
                    popup('end')

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                create_popup()
            if event.key == pygame.K_ESCAPE:
                messageBox = ctypes.windll.user32.MessageBoxW
                value = messageBox(None, 'Exit ? ',"Pause",0x70 | 0x2)
                if value == 5:
                    print('Nichts')
                elif value == 4:
                    print('Restart')
                elif value == 3:
                    print('Hauptmenu')
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
