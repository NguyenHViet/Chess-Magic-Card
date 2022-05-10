import random

import pygame
import sys
import time

import chess
import effect
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
usedCard = False
env = 'Desert'

SETTINGS = {
    'Music Volumn': 0.1,
    'Sound Volumn': 0,
    'Time': 180,
    'Time Bonus': 10,
    'AddTimeable': True,
    'TotalActions': 15,
}

pygame.display.set_caption("Chess: Magic Card")
ncard = card.CardArea(HEIGHT, WIDTH, offsetHeight, offsetWidth, init.listImage)
nboard = board.Board(offsetHeight, offsetWidth, WIDTH, 'w', init.ENVIRONMENT[env], init.listImage)
Players = [player.Player('Player 1', 'w'), player.Player('Player 2', 'b')]
clock = pygame.time.Clock()

pause = True
turns = 0
phase = chess.PHASE['Start']

def turn_off_music():
    pygame.mixer.music.set_volume(0)

def turn_on_music():
    pygame.mixer.music.set_volume(SETTINGS['Music Volumn'])

def new_game():
    global turns, phase, nboard, ncard, Players, startTurnTime, env
    startTurnTime = math.floor(time.time())
    turns = 0
    phase = chess.PHASE['Start']
    pause = False
    if env == 'Random':
        env = random.choice(['Desert', 'Frozen River', 'Foggy Forest', 'Swamp', 'Grassland'])
    nboard = board.Board(offsetHeight, offsetWidth, WIDTH, 'w', init.ENVIRONMENT[env], init.listImage)
    Players = [player.Player('Player 1', 'w', SETTINGS['Time'], SETTINGS['Time Bonus']), player.Player('Player 2', 'b', SETTINGS['Time'], SETTINGS['Time Bonus'])]
    pygame.mixer.music.load('music\\Two Steps From Hell - Victory (Instrumental).wav')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    turn_off_music()
    main()

def setting_game():
    global env, SETTINGS

    def add_min():
        SETTINGS['Time'] += 60
        pygame.time.delay(150)

    def add_second():
        temp = SETTINGS['Time']%60
        SETTINGS['Time'] -= temp
        temp = (temp+1)%60
        SETTINGS['Time'] += temp
        pygame.time.delay(150)

    def add_time_bonus():
        SETTINGS['Time Bonus'] += 1
        pygame.time.delay(150)

    def minus_min():
        if SETTINGS['Time']//60<=0:
            return
        SETTINGS['Time'] -= 60
        pygame.time.delay(150)

    def minus_second():
        temp = SETTINGS['Time'] % 60
        SETTINGS['Time'] -= temp
        temp = (temp - 1) % 60
        SETTINGS['Time'] += temp
        pygame.time.delay(150)

    def minus_time_bonus():
        if SETTINGS['Time Bonus']<=0:
            return
        SETTINGS['Time Bonus'] -= 1
        pygame.time.delay(150)

    def next_env():
        global env
        temp = list(init.ENVIRONMENT)
        try:
            env = temp[temp.index(env) + 1]
        except:
            env = temp[0]
        pygame.time.delay(150)

    def precious_env():
        global env
        temp = list(init.ENVIRONMENT)
        try:
            env = temp[temp.index(env) - 1]
        except:
            env = temp[-1]
        pygame.time.delay(150)

    x = 100
    while pause:
        textSurface = init.font60.render('TÙY CHỈNH', True, 'white')
        textRect = textSurface.get_rect()
        interval = (WinHeight - offsetHeight) / 6
        textRect.center = ((WinWidth / 2), offsetHeight * 2 - 50)
        cell.Cell(0, 0, init.listImage[env]['Background']).draw(WIN, WinHeight, WinWidth)
        WIN.blit(pygame.transform.scale(init.listImage['GEI']['Darker'], (WIDTH, WinHeight)), (offsetWidth, 0))
        WIN.blit(textSurface, textRect)
        timeLeft = '{:02}'.format(SETTINGS['Time'] // 60) + '   :   ' + '{:02}'.format(SETTINGS['Time'] % 60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
        button(timeLeft, init.listImage['GUI']['White Timer'], '', (WinWidth / 2) - 225, 400 - x, 300, 100, font=init.font50)
        WIN.blit(init.font15.render('THỜI GIAN TỔNG', True, 'black'), ((WinWidth / 2) - 140, 402 - x))
        WIN.blit(init.font15.render('PHÚT', True, 'black'), ((WinWidth / 2) - 170, 477 - x))
        WIN.blit(init.font15.render('GIÂY', True, 'black'), ((WinWidth / 2) - 20, 477 - x))
        button(str(SETTINGS['Time Bonus']), init.listImage['GUI']['White Timer'], '', (WinWidth / 2) + 125, 400 - x, 100, 100, font=init.font50)
        WIN.blit(init.font15.render('THƯỞNG', True, 'black'), ((WinWidth / 2) + 140, 402 - x))
        WIN.blit(init.font15.render('GIÂY', True, 'black'), ((WinWidth / 2) + 155, 477 - x))
        button('', init.listImage['GUI']['Arrow_Up'], '', (WinWidth / 2) - 180, 330 - x, 60, 50, add_min)
        button('', init.listImage['GUI']['Arrow_Up'], '', (WinWidth / 2) - 30, 330 - x, 60, 50, add_second)
        button('', init.listImage['GUI']['Arrow_Up'], '', (WinWidth / 2) + 145, 330 - x, 60, 50, add_time_bonus)
        button('', init.listImage['GUI']['Arrow_Down'], '', (WinWidth / 2) - 180, 520 - x, 60, 50, minus_min)
        button('', init.listImage['GUI']['Arrow_Down'], '', (WinWidth / 2) - 30, 520 - x, 60, 50, minus_second)
        button('', init.listImage['GUI']['Arrow_Down'], '', (WinWidth / 2) + 145, 520 - x, 60, 50, minus_time_bonus)

        button('', init.listImage['GUI']['Arrow_Right'], '', (WinWidth / 2) + 245, 720 - x, 50, 60, next_env)
        button('', init.listImage['GUI']['Arrow_Left'], '', (WinWidth / 2) - 295, 720 - x, 50, 60, precious_env)
        button(env, init.listImage[env]['Background'], init.listImage['GEI']['Darken'], (WinWidth / 2) - 200, 620 - x, 400, 250, new_game, color='white')

        button('BẮT ĐẦU!', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363 / 2, 800, 363, 100, new_game)
        pygame.display.update()

def mouse_on_board(pos):
    if pos[0] > offsetWidth and pos[0] < offsetWidth + WIDTH and pos[1] > offsetHeight and pos[1] < offsetHeight + HEIGHT:
        return True
    return False
def mouse_on_cards(pos):
    if pos[0] > offsetWidth + WIDTH + 55 and pos[0] < WinWidth and pos[1] > offsetHeight and pos[1] < offsetHeight + HEIGHT:
        return True
    return False

def updateGUI():
    global phase, turns, timing
    nowTime = math.floor(time.time())
    timing = nowTime - startTurnTime

    timeLeft = '{:02}'.format((Players[1].get_time() - (turns%2)*timing)//60) + ':' + '{:02}'.format((Players[1].get_time() - (turns%2)*timing)%60)
    button(timeLeft, init.listImage['GUI']['Black Timer'], '', 125, offsetHeight, 230, 60 ,color = 'white')
    button(str(Players[1].get_action()), init.listImage['GUI']['Actions'], '', 300, offsetHeight + 5, 50, 50, color='white')
    button(str(Players[1].get_totalAction()), init.listImage['GUI']['Actions'], '', 330, offsetHeight + 35, 30, 30, font=init.font20)

    timeLeft = '{:02}'.format((Players[0].get_time() - ((turns+1)%2)*timing)//60) + ':' + '{:02}'.format((Players[0].get_time() - ((turns+1)%2)*timing)%60)
    button(timeLeft, init.listImage['GUI']['White Timer'], '', 125, offsetHeight + 100, 230, 60)
    button(str(Players[0].get_action()), init.listImage['GUI']['Actions'], '', 300, offsetHeight + 105, 50, 50, color='white')
    button(str(Players[0].get_totalAction()), init.listImage['GUI']['Actions'], '', 330, offsetHeight + 135, 30, 30, font=init.font20)

    button('', init.listImage['GUI']['Lock'], '', 125, offsetHeight + (turns%2)*100, 230, 60)
    if Players[turns%2].get_time() - timing < 0:
        turns += 1
        endGame()

    button("", init.listImage['GUI']['EndTurn'], init.listImage['GUI']['Choice'], 35, offsetHeight, 160, 160, end_turn)
    button("", init.listImage['GUI']['Pause'], init.listImage['GUI']['Choice'], 25, 25, 50, 50, paused)

    for i in range(len(Players[turns%2].get_cards())):
        button("", init.listImage['GUI']['Random'], init.listImage['GUI']['Choice'], offsetWidth + WIDTH + 10, offsetHeight + (HEIGHT/3)*i + (HEIGHT)/8, 50, 50, Players[turns%2].redraw_card, param = i)

    if pygame.mixer.music.get_busy():
        button("", init.listImage['GUI']['Pause'], '', 90, 40, 30, 30, turn_off_music)
    else:
        button("", init.listImage['GUI']['Pause'], '', 90, 40, 30, 30, turn_on_music)

    button('Turn: {:<12}'.format(turns), init.listImage['GUI']['Turn Phase'], '', 45, offsetHeight + 200, 320, 100, font=init.font30)
    WIN.blit(init.listImage['GUI']['Turn Phase Ef'], (45, offsetHeight + 200))

def update_display(win, nboard, pos, turns, phase):
    WIN.fill('white')
    nboard.draw(win)
    ncard.draw(win, init.font40, pos, Players[turns%2])
    if phase == chess.PHASE['Finish']:
        print('WIN')
        endGame()
    updateGUI()
    pygame.display.update()

def main():
    turn_on_music()
    global pause, phase, turns, startTurnTime, timing
    redraw = False
    pause = False
    selected = False
    required = 0
    selectedPos = []
    playingTeam = 'w'
    while True:
        if phase == chess.PHASE['Start']:
            usedCard = False
            selected = False
            required = 0
            selectedPos = []
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
                elif mouse_on_cards(pos) and phase == chess.PHASE['Picking'] and not usedCard:
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
                            nboard.deselect()
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
                        phase = Players[turns % 2].update((chess.PHASE['End']), init.DECK, False, startTurnTime)
                        selected = False
                        selectedPos = []
                        usedCard = True
                        #-----------------------------------------------------------------------------------------------
                print(" Phase:", phase)
                nboard.printMap()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused()
        check_evolutions()
        phase = Players[turns % 2].update(phase, init.DECK, SETTINGS['AddTimeable'], startTurnTime)
        if phase == chess.PHASE['End']:
            startTurnTime = math.floor(time.time())
        phase, turns = nboard.update(phase, turns)
        update_display(WIN, nboard, pygame.mouse.get_pos(), turns, phase)

def button(text, img, img_h, x, y, width, height, action = None, color = 'black', font = init.font40, **param):
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
            if param != {}:
                action(param)
            else:
                action()
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    WIN.blit(textSurface, textRect)

def paused():
    pygame.mixer.music.pause()
    global pause
    pause = True
    textSurface = init.font60.render('TẠM DỪNG', True, 'white')
    textRect = textSurface.get_rect()
    interval = (WinHeight - offsetHeight) / 6
    textRect.center = ((WinWidth / 2), offsetHeight*2)
    while pause:
        cell.Cell(0, 0, init.listImage[env]['Background']).draw(WIN, WinHeight, WinWidth)
        WIN.blit(pygame.transform.scale(init.listImage['GEI']['Darker'], (WIDTH, WinHeight)), (offsetWidth, 0))
        WIN.blit(textSurface, textRect)
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
    pygame.mixer.music.pause()
    global pause
    pause = True
    textSurface = init.font60.render('Player ' + str(turns%2 + 1) + ' WIN', True, 'white')
    textRect = textSurface.get_rect()
    interval = (WinHeight - offsetHeight) / 6
    textRect.center = ((WinWidth / 2), offsetHeight*2)
    while pause:
        cell.Cell(0, 0, init.listImage[env]['Background']).draw(WIN, WinHeight, WinWidth)
        WIN.blit(pygame.transform.scale(init.listImage['GEI']['Darker'], (WIDTH, WinHeight)), (offsetWidth, 0))
        WIN.blit(textSurface, textRect)
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

def end_game():
    pygame.quit()
    quit()

def check_evolutions():

    def evolution(param):
        if param['team'] == 'w':
            direction = 'upwward'
        else:
            direction = 'downward'
        newChess = getattr(chess, param['type'])(param['team'], direction, init.listImage[param['team']][param['type']])
        param['oBoard'][param['index']] = newChess
        main()

    if phase == chess.PHASE['End']:
        oBoard = nboard.getoBoard()
        for object in oBoard.items():
            try:
                if object[1].get_type() == 'Pawn' and object[0][1] == 7*(object[1].get_direction()):
                    WIN.blit(pygame.transform.scale(init.listImage['GEI']['Darker'], (WinWidth, WinHeight)), (0, 0))
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                end_game()
                        button('', init.listImage['Chess Art']['Queen'], init.listImage['GEI']['Darken'], WinWidth/2 - 315, WinHeight/2 - 200, 150, 322, evolution, type='Queen', team = object[1].get_team(), oBoard = oBoard, index = object[0])
                        button('', init.listImage['Chess Art']['Bishop'], init.listImage['GEI']['Darken'], WinWidth/2 - 155, WinHeight/2 - 122, 150, 322, evolution, type='Bishop', team = object[1].get_team(), oBoard = oBoard, index = object[0])
                        button('', init.listImage['Chess Art']['Knight'], init.listImage['GEI']['Darken'], WinWidth/2 + 5, WinHeight/2 - 200, 150, 322, evolution, type='Knight', team = object[1].get_team(), oBoard = oBoard, index = object[0])
                        button('', init.listImage['Chess Art']['Rook'], init.listImage['GEI']['Darken'], WinWidth/2 + 165, WinHeight/2 - 122, 150, 322, evolution, type='Rook', team = object[1].get_team(), oBoard = oBoard, index = object[0])
                        pygame.display.update()
            except:
                pass

def game_intro():
    pygame.time.delay(80)
    global pause
    pause = True
    textSurface = init.font60.render('CHESS: MAGIC CARD', True, 'white')
    textRect = textSurface.get_rect()
    interval = (WinHeight - offsetHeight) / 6
    textRect.center = ((WinWidth / 2), offsetHeight*2)
    while pause:
        cell.Cell(0, 0, init.listImage['Foggy Forest']['Background']).draw(WIN, WinHeight, WinWidth)
        WIN.blit(pygame.transform.scale(init.listImage['GEI']['Darker'], (WIDTH, WinHeight)), (offsetWidth, 0))
        WIN.blit(textSurface, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
        button('BẮT ĐẦU', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363/2, 2*interval, 363, 100, setting_game)
        button('THOÁT', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363/2, 3*interval, 363, 100, end_game)
        pygame.display.update()

game_intro()