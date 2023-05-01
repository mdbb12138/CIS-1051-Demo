import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((450,450))
pygame.display.set_caption('Gomoku')
board_background = pygame.image.load('Pictures/board.jpg')
board = [[0 for i in range(15)] for j in range(15)]
player = 1

def draw_board():
    for row in range(15):
        for col in range(15):
            if board[row][col] == 1:
                pygame.draw.circle(screen, (0, 0, 0), (col * 30 + 15, row * 30 + 15), 13)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, (255, 255, 255), (col * 30 + 15, row * 30 + 15), 13)

def check_win(board, player):
    for i in range(15):
        for j in range(11):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player and board[i][j+4] == player:
                return True
    for i in range(11):
        for j in range(15):
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player and board[i+4][j] == player:
                return True
    for i in range(11):
        for j in range(11):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player and board[i+4][j+4] == player:
                return True
            if board[i][j+4] == player and board[i+1][j+3] == player and board[i+2][j+2] == player and board[i+3][j+1] == player and board[i+4][j] == player:
                return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // (450 // 15)
            col = x // (450 // 15)
            if board[row][col] == 0:
                board[row][col] = player
                if player == 1:
                    player = 2
                else:
                    player = 1
    screen.blit(board_background,(0,0))
    draw_board()
    if player == 1:
        pygame.draw.circle(screen, (0, 0, 0), (30, 430), 13)
    else:
        pygame.draw.circle(screen, (255, 255, 255), (30, 430), 13)
    pygame.display.update()
    if check_win(board, 1):
        print("Player 1 wins!")
        #pygame.quit()
        exit()
    elif check_win(board, 2):
        print("Player 2 wins!")
        #pygame.quit()
        exit()

