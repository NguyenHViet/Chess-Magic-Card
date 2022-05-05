import pygame
import sys
import time

import chess
import init
import cell
import board
import enviroment
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

pygame.display.set_caption("Chess: Magic Card")
ncard = card.CardArea(HEIGHT, WIDTH, offsetHeight, offsetWidth, init.listImage)
nboard = board.Board(offsetHeight, offsetWidth, WIDTH, 'w', init.ENVIRONMENT['Desert'], init.listImage)
Players = [player.Player('Player 1', 'w'), player.Player('Player 2', 'b')]
pause = True
turns = 0
phase = chess.PHASE['Start']

def new_game():
    turns = 0
    phase = chess.PHASE['Start']
    pause = False
    nboard = board.Board(offsetHeight, offsetWidth, WIDTH, 'w', init.ENVIRONMENT['Desert'], init.listImage)
    Players = [player.Player('Player 1', 'w'), player.Player('Player 2', 'b')]
    pygame.mixer.music.load('music\\Two Steps From Hell - Star Sky.wav')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.pause()

def mouse_on_board(pos):
    if pos[0] > offsetWidth and pos[0] < offsetWidth + WIDTH and pos[1] > offsetHeight and pos[1] < offsetHeight + HEIGHT:
        return True
    return False
def mouse_on_cards(pos):
    if pos[0] > offsetWidth + WIDTH and pos[0] < WinWidth and pos[1] > offsetHeight and pos[1] < offsetHeight + HEIGHT:
        return True
    return False

def update_display(win, nboard, pos, turns, phase):
    WIN.fill('white')
    ncard.draw(win, init.font20, pos, Players[turns%2].get_cards(), Players[turns%2].get_picking())
    nboard.draw(win)
    if phase == chess.PHASE['Finish']:
        WIN.fill("black")
    button("", init.listImage['GUI']['EndTurn'], init.listImage['GUI']['Choice'], 10, offsetHeight, 160, 160, end_turn)
    button("", init.listImage['GUI']['Pause'], init.listImage['GUI']['Choice'], 50, 50, 50, 50, paused)
    pygame.display.update()

def main():
    pygame.mixer.music.unpause()
    global pause, phase, turns
    pause = False
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
                            if nboard.select_Move(selectedPos, index):
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
                        phase = Players[turns % 2].update((chess.PHASE['Picking']), init.DECK, 0, False)
                        selected = False
                        selectedPos = []
                        #-----------------------------------------------------------------------------------------------
                print(" Phase:", phase)
                nboard.printMap()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused()
        Players[turns % 2].update(phase, init.DECK, 0, False)
        phase, turns = nboard.update(phase, turns)
        update_display(WIN, nboard, pygame.mouse.get_pos(), turns, phase)

def button(text, img, img_h, x, y, width, height, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    img = pygame.transform.scale(img, (width, height))
    img_h = pygame.transform.scale(img_h, (width, height))
    WIN.blit(img, (x, y))
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        WIN.blit(img_h, (x, y))
        if click[0] == 1 and action != None:
            action()
    textSurface = init.font20.render(text, True, 'black')
    textRect = textSurface.get_rect()
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    WIN.blit(textSurface, textRect)

def paused():
    pygame.mixer.music.pause()
    global pause
    pause = True
    textSurface = init.font20.render('Pause', True, 'black')
    textRect = textSurface.get_rect()
    textRect.center = ((WinWidth / 2), (WinHeight / 2))
    cell.Cell(0, 0, init.listImage["GEI"]['Darken']).draw(WIN, WinHeight, WinWidth)
    WIN.blit(textSurface, textRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
        button("Chơi Tiếp", init.listImage['b']['p'], init.listImage['b']['k'], 100, 100, 100, 100, main)
        pygame.display.update()

def end_turn():
    global phase, turns
    turns += 1
    phase = chess.PHASE['End']

def game_intro():
    pass

new_game()
main()