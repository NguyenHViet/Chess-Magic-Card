import pygame
import sys
import time

import chess
import init
import cell
import board
import environment
import card
import player
import math

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

startTurnTime = math.floor(time.time())
timing = 0
AddTimeAble = True
env = 'Desert'

pygame.display.set_caption("Chess: Magic Card")
ncard = card.CardArea(HEIGHT, WIDTH, offsetHeight, offsetWidth, init.listImage)
nboard = board.Board(offsetHeight, offsetWidth, WIDTH, 'w', init.ENVIRONMENT[env], init.listImage)
Players = [player.Player('Player 1', 'w'), player.Player('Player 2', 'b')]
clock = pygame.time.Clock()

pause = True
turns = 0
phase = chess.PHASE['Start']

def new_game():
    global turns, phase, nboard, ncard, Players, startTurnTime
    startTurnTime = math.floor(time.time())
    turns = 0
    phase = chess.PHASE['Start']
    pause = False
    nboard = board.Board(offsetHeight, offsetWidth, WIDTH, 'w', init.ENVIRONMENT[env], init.listImage)
    Players = [player.Player('Player 1', 'w', 120, 10), player.Player('Player 2', 'b', 120, 10)]
    pygame.mixer.music.load('music\\Two Steps From Hell - Star Sky.wav')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.pause()

    main()

def mouse_on_board(pos):
    if pos[0] > offsetWidth and pos[0] < offsetWidth + WIDTH and pos[1] > offsetHeight and pos[1] < offsetHeight + HEIGHT:
        return True
    return False
def mouse_on_cards(pos):
    if pos[0] > offsetWidth + WIDTH and pos[0] < WinWidth and pos[1] > offsetHeight and pos[1] < offsetHeight + HEIGHT:
        return True
    return False

def updateGUI():
    global phase, turns, timing
    nowTime = math.floor(time.time())
    timing = nowTime - startTurnTime

    timeLeft = '{:02}'.format((Players[1].get_time() - (turns%2)*timing)//60) + ':' + '{:02}'.format((Players[1].get_time() - (turns%2)*timing)%60)
    button(timeLeft, init.listImage['GUI']['Black Timer'], '', 125, offsetHeight, 230, 60 ,color = 'white')
    button(str(Players[1].get_action()), init.listImage['GUI']['Actions'], '', 300, offsetHeight + 5, 50, 50, color='white')

    timeLeft = '{:02}'.format((Players[0].get_time() - ((turns+1)%2)*timing)//60) + ':' + '{:02}'.format((Players[0].get_time() - ((turns+1)%2)*timing)%60)
    button(timeLeft, init.listImage['GUI']['White Timer'], '', 125, offsetHeight + 100, 230, 60)
    button(str(Players[0].get_action()), init.listImage['GUI']['Actions'], '', 300, offsetHeight + 105, 50, 50, color='white')

    button('', init.listImage['GUI']['Lock'], '', 125, offsetHeight + (turns%2)*100, 230, 60)
    if Players[turns%2].get_time() - timing < 0:
        endGame()

    button("", init.listImage['GUI']['EndTurn'], init.listImage['GUI']['Choice'], 35, offsetHeight, 160, 160, end_turn)
    button("", init.listImage['GUI']['Pause'], init.listImage['GUI']['Choice'], 25, 25, 50, 50, paused)

def update_display(win, nboard, pos, turns, phase):
    WIN.fill('white')
    ncard.draw(win, init.font40, pos, Players[turns%2])
    nboard.draw(win)
    if phase == chess.PHASE['Finish']:
        print('WIN')
        endGame()
    updateGUI()
    pygame.display.update()

def main():
    pygame.mixer.music.unpause()
    global pause, phase, turns, startTurnTime, timing
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
                end_game()

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
                                else:
                                    phase = chess.PHASE['Picking']
                            else:
                                selected = False
                        except:
                            selectedPos = []
                            phase = chess.PHASE['Picking']
                    elif len(selectedPos) <= required and selected and mouse_on_board(pos):
                        nboard.deselect()
                        index = nboard.find_Cell(pos)
                        result = Players[turns%2].play_card(nboard, selectedPos + [index])
                        if 'Fail' not in result:
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
                        phase = Players[turns % 2].update((chess.PHASE['Picking']), init.DECK, False, startTurnTime)
                        selected = False
                        selectedPos = []
                        #-----------------------------------------------------------------------------------------------
                print(" Phase:", phase)
                nboard.printMap()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused()
        phase = Players[turns % 2].update(phase, init.DECK, AddTimeAble, startTurnTime)
        if phase == chess.PHASE['End']:
            startTurnTime = math.floor(time.time())
        phase, turns = nboard.update(phase, turns)
        update_display(WIN, nboard, pygame.mouse.get_pos(), turns, phase)

def button(text, img, img_h, x, y, width, height, action = None, color = 'black'):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    img = pygame.transform.scale(img, (width, height))
    WIN.blit(img, (x, y))
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        try:
            img_h = pygame.transform.scale(img_h, (width, height))
            WIN.blit(img_h, (x, y))
        except:
            pass
        if click[0] == 1 and action != None:
            action()
    textSurface = init.font40.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    WIN.blit(textSurface, textRect)

def paused():
    pygame.mixer.music.pause()
    global pause
    pause = True
    textSurface = init.font60.render('TẠM DỪNG', True, 'black')
    textRect = textSurface.get_rect()
    interval = (WinHeight - offsetHeight) / 6
    textRect.center = ((WinWidth / 2), offsetHeight*2)
    cell.Cell(0, 0, init.listImage['GEI']['Normal']).draw(WIN, WinHeight, WinWidth)
    WIN.blit(textSurface, textRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main()
        button('CHƠI TIẾP', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363/2, 2*interval, 363, 100, main)
        button('CHƠI MỚI', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363/2, 3*interval, 363, 100, new_game)
        button('MENU', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363/2, 4*interval, 363, 100, game_intro)
        button('THOÁT', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363/2, 5*interval, 363, 100, end_game)
        pygame.display.update()

def endGame():
    pygame.time.delay(50)
    pygame.mixer.music.pause()
    global pause
    pause = True
    textSurface = init.font60.render('Player ' + str(turns%2 + 1) + ' WIN', True, 'black')
    textRect = textSurface.get_rect()
    interval = (WinHeight - offsetHeight) / 6
    textRect.center = ((WinWidth / 2), offsetHeight*2)
    cell.Cell(0, 0, init.listImage['GEI']['Normal']).draw(WIN, WinHeight, WinWidth)
    WIN.blit(textSurface, textRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
        button('CHƠI LẠI', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363/2, 2*interval, 363, 100, new_game)
        button('MENU', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363/2, 3*interval, 363, 100, game_intro)
        button('THOÁT', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363/2, 4*interval, 363, 100, end_game)
        pygame.display.update()

def end_turn():
    global phase, nboard, turns
    Players[turns % 2].decelect()
    nboard.deselect()
    phase = chess.PHASE['End']
    pygame.time.delay(50)

def end_game():
    pygame.quit()
    quit()

def game_intro():
    global pause
    pause = True
    textSurface = init.font60.render('CHESS: MAGIC CARD', True, 'black')
    textRect = textSurface.get_rect()
    interval = (WinHeight - offsetHeight) / 6
    textRect.center = ((WinWidth / 2), offsetHeight*2)
    cell.Cell(0, 0, init.listImage['GEI']['Normal']).draw(WIN, WinHeight, WinWidth)
    WIN.blit(textSurface, textRect)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
        button('BẮT ĐẦU', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363/2, 2*interval, 363, 100, new_game)
        button('THOÁT', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363/2, 3*interval, 363, 100, end_game)
        pygame.display.update()

game_intro()