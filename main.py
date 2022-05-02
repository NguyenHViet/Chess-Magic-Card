import pygame
import sys
import time

import chess
import init
import board
import card
import player

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
1: Suy Nghĩ
2: Chơi cờ
3: Chơi bài
4: Kết thúc lượt
5: Kết thúc trận
'''

pygame.display.set_caption("Chess: Magic Card")

nboard = board.Board(offsetHeight, offsetWidth, WIDTH, 'w', 'classic', init.listImage)
def mouse_on_board(pos):
    if pos[0] > offsetWidth and pos[0] < offsetWidth + WIDTH and pos[1] > offsetHeight and pos[1] < offsetHeight + HEIGHT:
        return True
    return False
ncard = card.CardArea(HEIGHT, WIDTH, offsetHeight, offsetWidth, init.listImage)
def mouse_on_cards(pos):
    if pos[0] > offsetWidth + WIDTH and pos[0] < WinWidth and pos[1] > offsetHeight and pos[1] < offsetHeight + HEIGHT:
        return True
    return False
Players = [player.Player('Player 1', 'w'), player.Player('Player 2', 'b')]

def update_display(win, nboard, pos, turns):
    WIN.fill("white")
    ncard.draw(win, init.font, pos, Players[turns%2].get_cards())
    nboard.draw(win)
    pygame.display.update()

def main(WIN, WIDTH):
    turns = 0
    phase = chess.PHASE['Start']
    selected = False
    required = 0
    selectedPos = []
    playingTeam = 'w'
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
                pos = pygame.mouse.get_pos()
                index = nboard.find_Cell(pos)
                if mouse_on_board(pos) and phase == chess.PHASE['Picking']:
                    phase = chess.PHASE['Move']
                elif mouse_on_cards(pos) and phase == chess.PHASE['Picking']:
                    phase = chess.PHASE['Cast']

                if event.button == 3:
                    nboard.deselect()
                    Players[turns%2].decelect()
                    phase = chess.PHASE['Picking']
                    selected = False
                    selectedPos = []
                elif event.button in [2, 4, 5]:
                    break

                if phase == chess.PHASE['Move']:
                    if selected == False:
                        try:
                            nboard.deselect()
                            selected = nboard.select_Chess(index, phase, playingTeam)
                            selectedPos = index
                        except:
                            selectedPos = []
                            phase = chess.PHASE['Picking']
                    else:
                        try:
                            new_turns = nboard.select_Move(selectedPos, index, turns)
                            if new_turns > turns:
                                turns = new_turns
                                phase = chess.PHASE['End']
                            else:
                                phase = chess.PHASE['Picking']
                            selected = False
                            selectedPos = []
                        except:
                            phase = chess.PHASE['Picking']
                        #-----------------------------------------------------------------------------------------------
                elif phase == chess.PHASE['Cast']:
                    if selected == False:
                        try:
                            index = ncard.pick_card(pos)
                            if index != None:
                                required = Players[turns % 2].pick_card(index)
                                if required != -1:
                                    selected = True
                        except:
                            selectedPos = []
                            phase = chess.PHASE['Picking']
                    elif len(selectedPos) <= required and selected and mouse_on_board(pos):
                        nboard.deselect()
                        index = nboard.find_Cell(pos)
                        if Players[turns%2].play_card(nboard, selectedPos + [index]) != 'Fail':
                            selectedPos.append(index)
                    else:
                        Players[turns%2].decelect()
                        selectedPos = []
                        phase = chess.PHASE['Picking']
                        selected = False
                    # Nếu đã đủ số lượng đối tượng
                    if len(selectedPos) == required:
                        nboard.deselect()
                        Players[turns % 2].decelect()
                        phase = chess.PHASE['Picking']
                        selected = False
                        selectedPos = []
                        #-----------------------------------------------------------------------------------------------
                print(" Phase:", phase)
                nboard.printMap()
        Players[turns % 2].update(phase, init.DECK, 0, False)
        phase = nboard.update(phase)
        update_display(WIN, nboard, pygame.mouse.get_pos(), turns)


main(WIN, WIDTH)