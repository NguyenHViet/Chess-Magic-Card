import pygame
import sys
import time
import init
import chess
import board
import cell

pygame.init()

# Kích thước window
WinWidth = 1600
WinHeight = 1000
# Kích thước sàn đấu
WIDTH = 800
HEIGHT = 800
offsetWidth = (WinWidth - WIDTH)/2
offsetHeight = (WinHeight - HEIGHT)/2
WIN = pygame.display.set_mode((WinWidth, WinHeight))
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

'''
Các giai đoạn trong lượt
0: Đầu lượt đi
1: Chơi cờ
2: Chời bài
3: Kết thúc lượt
4: Kết thúc trận
'''

pygame.display.set_caption("Chess: Magic Card")
WIN.fill("white")

nboard = board.Board(offsetHeight, offsetWidth, WIDTH, 'w', 'classic', init.listImage)

def update_display(win, nboard):

    nboard.draw(win)
    pygame.display.update()

def main(WIN, WIDTH):
    turns = 0
    phase = 0
    selected = False
    originPos = []
    playingTeam = 'b'
    player1Team = 'w'
    player2Team = 'b'
    while True:
        if turns % 2 == 0:
            playingTeam = 'w'
        else:
            playingTeam = 'b'
        pygame.time.delay(50) ##stops cpu dying
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            """This quits the program if the player closes the window"""

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(" Phase:", phase)
                pos = pygame.mouse.get_pos()
                if selected == False and phase == 1:
                    try:
                        nboard.deseclect()
                        selected = nboard.select_Chess(pos, phase, playingTeam)
                        originPos = pos
                    except:
                        originPos = []
                else:
                    try:
                        new_turns = nboard.select_Move(originPos, pos, turns)
                        if new_turns > turns:
                            turns = new_turns
                            phase = 3
                        selected = False
                    except:
                        pass

            phase = nboard.update(phase)
            update_display(WIN, nboard)


main(WIN, WIDTH)