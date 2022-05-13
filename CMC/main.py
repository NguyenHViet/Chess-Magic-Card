import random

import pygame
import time

import CMC.chess as chess
import CMC.init as init
import CMC.cell as cell
import CMC.board as board
import CMC.card as card
import CMC.player as player
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

# Khởi tạo các giá trị global
startTurnTime = math.floor(time.time())
timing = 0
click = 0
env = 'Grassland'
MUSIC_END = pygame.USEREVENT + 1


pygame.display.set_caption("Chess: Magic Card")
ncard = card.CardArea(HEIGHT, WIDTH, offsetHeight, offsetWidth, init.listImage)
nboard = board.Board(offsetHeight, offsetWidth, WIDTH, 'w', init.ENVIRONMENT[env], init.listImage)
Players = [player.Player('Player 1', 'w'), player.Player('Player 2', 'b')]
clock = pygame.time.Clock()
playingTeam = 'w'

pause = True
turns = 0
phase = chess.PHASE['Start']

def turn_off_music(id = 0):
    """
    Tạm dừng nhạc nền
    :return: None
    """
    pygame.mixer.music.pause()

def turn_on_music():
    """
    Chạy tiếp nhạc nền
    :return: None
    """
    pygame.mixer.music.unpause()

def new_game():
    """
    Khởi tạo các giá trị và tạo ván đấu mới
    :return: None
    """
    global turns, phase, nboard, ncard, Players, startTurnTime, env
    init.HistoryLog = [' ' for i in range (6)]
    init.HistoryLog.append('New Round!')
    random.shuffle(init.listMusic)
    pygame.mixer.music.load(init.listMusic[0])
    init.listMusic.append(init.listMusic.pop(0))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(init.SETTINGS['Music Volumn'] / 100)
    pygame.mixer.music.queue(init.listMusic[0])
    init.listMusic.append(init.listMusic.pop(0))
    pygame.mixer.music.set_endevent(MUSIC_END)
    startTurnTime = math.floor(time.time())
    turns = 0
    phase = chess.PHASE['Start']
    pause = False
    if env == 'Random':
        env = random.choice(['Desert', 'Frozen River', 'Foggy Forest', 'Swamp', 'Grassland'])
    nboard = board.Board(offsetHeight, offsetWidth, WIDTH, 'w', init.ENVIRONMENT[env], init.listImage)
    Players = [player.Player('Player 1', 'w', init.SETTINGS['Time'], init.SETTINGS['Time Bonus']), player.Player('Player 2', 'b', init.SETTINGS['Time'], init.SETTINGS['Time Bonus'])]
    turn_off_music()
    main()

def setting_game():
    """
    Cài dặt các thông số trong trận đấu
    :return: None
    """
    global env, SETTINGS
    pygame.time.delay(50)

    def add_min(param):
        if init.SETTINGS['Time'] // 60 <= 0:
            return
        init.SETTINGS['Time'] += param['value']
        pygame.time.delay(50)

    def add_second(param):
        temp = init.SETTINGS['Time'] % 60
        init.SETTINGS['Time'] -= temp
        temp = (temp + param['value'])%60
        init.SETTINGS['Time'] += temp
        pygame.time.delay(50)

    def add_time_bonus(param):
        if init.SETTINGS['Time Bonus'] <= 0:
            return
        init.SETTINGS['Time Bonus'] += param['value']
        pygame.time.delay(50)

    def next_env(param):
        global env
        temp = list(init.ENVIRONMENT)
        try:
            env = temp[temp.index(env) + param['value']]
        except:
            env = temp[0]
        pygame.time.delay(50)

    x = 100
    while pause:
        textSurface = init.font60.render('TÙY CHỈNH', True, 'white')
        textRect = textSurface.get_rect()
        interval = (WinHeight - offsetHeight) / 6
        textRect.center = ((WinWidth / 2), offsetHeight * 2 - 50)
        cell.Cell(0, 0, init.listImage[env]['Background']).draw(WIN, WinHeight, WinWidth)
        WIN.blit(pygame.transform.scale(init.listImage['GEI']['Darker'], (WIDTH, WinHeight)), (offsetWidth, 0))
        WIN.blit(textSurface, textRect)
        timeLeft = '{:02}'.format(init.SETTINGS['Time'] // 60) + '   :   ' + '{:02}'.format(init.SETTINGS['Time'] % 60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
        drawTextImg(timeLeft, init.listImage['GUI']['White Timer'], (WinWidth / 2) - 225, 400 - x, 300, 100, font=init.font50)
        WIN.blit(init.font15.render('THỜI GIAN TỔNG', True, 'black'), ((WinWidth / 2) - 140, 402 - x))
        WIN.blit(init.font15.render('PHÚT', True, 'black'), ((WinWidth / 2) - 170, 477 - x))
        WIN.blit(init.font15.render('GIÂY', True, 'black'), ((WinWidth / 2) - 20, 477 - x))
        drawTextImg(str(init.SETTINGS['Time Bonus']), init.listImage['GUI']['White Timer'], (WinWidth / 2) + 125, 400 - x, 100, 100, font=init.font50)
        WIN.blit(init.font15.render('THƯỞNG', True, 'black'), ((WinWidth / 2) + 140, 402 - x))
        WIN.blit(init.font15.render('GIÂY', True, 'black'), ((WinWidth / 2) + 155, 477 - x))
        button('', init.listImage['GUI']['Arrow_Up'], '', (WinWidth / 2) - 180, 330 - x, 60, 50, add_min, value = 60)
        button('', init.listImage['GUI']['Arrow_Up'], '', (WinWidth / 2) - 30, 330 - x, 60, 50, add_second, value = 1)
        button('', init.listImage['GUI']['Arrow_Up'], '', (WinWidth / 2) + 145, 330 - x, 60, 50, add_time_bonus, value = 1)
        button('', init.listImage['GUI']['Arrow_Down'], '', (WinWidth / 2) - 180, 520 - x, 60, 50, add_min, value = -60)
        button('', init.listImage['GUI']['Arrow_Down'], '', (WinWidth / 2) - 30, 520 - x, 60, 50, add_second, value = -1)
        button('', init.listImage['GUI']['Arrow_Down'], '', (WinWidth / 2) + 145, 520 - x, 60, 50, add_time_bonus, value = -1)

        button('', init.listImage['GUI']['Arrow_Right'], '', (WinWidth / 2) + 245, 720 - x, 50, 60, next_env, value = 1)
        button('', init.listImage['GUI']['Arrow_Left'], '', (WinWidth / 2) - 295, 720 - x, 50, 60, next_env, value = -1)
        button(env, init.listImage[env]['Background'], init.listImage['GEI']['Darken'], (WinWidth / 2) - 200, 620 - x, 400, 250, new_game, color='white')

        button('BẮT ĐẦU!', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363 / 2, 800, 363, 100, new_game)
        pygame.display.update()

def mouse_on_board(pos):
    """
    Kiểm tra con trỏ chuột có nằm trên bàn cờ
    :param pos: Vị trí con trỏ chuột (tuple(int, int))
    :return: Kết quả (bool)
    """
    if pos[0] > offsetWidth and pos[0] < offsetWidth + WIDTH and pos[1] > offsetHeight and pos[1] < offsetHeight + HEIGHT:
        return True
    return False
def mouse_on_cards(pos):
    """
    Kiểm tra con trỏ chuột có nằm trên khu vực bài
    :param pos: Vị trí con trỏ chuột (tuple(int, int))
    :return: Kết quả (bool)
    """
    if pos[0] > offsetWidth + WIDTH + 55 and pos[0] < WinWidth and pos[1] > offsetHeight and pos[1] < offsetHeight + HEIGHT:
        return True
    return False

def updateGUI():
    """
    Cập nhập giao diện cùng các nút bấm
    :return: None
    """
    global phase, turns, timing

    button("", init.listImage['GUI']['Pause'], init.listImage['GUI']['Choice'], 25, 25, 50, 50, paused)

    nowTime = math.floor(time.time())
    timing = nowTime - startTurnTime
    timeLeft = '{:02}'.format((Players[1].get_time() - (turns%2)*timing)//60) + ':' + '{:02}'.format((Players[1].get_time() - (turns%2)*timing)%60)
    drawTextImg(timeLeft, init.listImage['GUI']['Black Timer'], 125, offsetHeight, 230, 60, color ='white')
    drawTextImg(str(Players[1].get_action()), init.listImage['GUI']['Actions'], 300, offsetHeight + 5, 50, 50, color='white')
    drawTextImg(str(Players[1].get_totalAction()), init.listImage['GUI']['Actions'], 330, offsetHeight + 35, 30, 30, font=init.font20)

    timeLeft = '{:02}'.format((Players[0].get_time() - ((turns+1)%2)*timing)//60) + ':' + '{:02}'.format((Players[0].get_time() - ((turns+1)%2)*timing)%60)
    drawTextImg(timeLeft, init.listImage['GUI']['White Timer'], 125, offsetHeight + 100, 230, 60)
    drawTextImg(str(Players[0].get_action()), init.listImage['GUI']['Actions'], 300, offsetHeight + 105, 50, 50, color='white')
    drawTextImg(str(Players[0].get_totalAction()), init.listImage['GUI']['Actions'], 330, offsetHeight + 135, 30, 30, font=init.font20)

    WIN.blit(init.listImage['GUI']['Lock'], (125, offsetHeight + (turns % 2) * 100))

    button('', init.listImage['GUI']['EndTurn'], init.listImage['GUI']['Choice'], 35, offsetHeight, 160, 160, end_turn)

    if Players[turns%2].get_time() - timing < 0:
        turns += 1
        endGame()

    for i in range(len(Players[turns%2].get_cards())):
        button("", init.listImage['GUI']['Random'], init.listImage['GUI']['Choice'], offsetWidth + WIDTH + 10, offsetHeight + (HEIGHT / 3) * i + (HEIGHT) / 8, 50, 50, Players[turns % 2].redraw_card, param = i)

    if pygame.mixer.music.get_busy():
        button("", init.listImage['GUI']['Mute'], init.listImage['GUI']['Choice'], 90, 40, 30, 30, turn_off_music)
    else:
        button("", init.listImage['GUI']['Unmute'], init.listImage['GUI']['Choice'], 90, 40, 30, 30, turn_on_music)

    drawTextImg('{}'.format(env), init.listImage['GUI']['Env Timer'], 45, offsetHeight + 200, 320, 100, font=init.font30)
    WIN.blit(init.listImage['GUI']['Env Timer Ef'], (48, offsetHeight + 200))
    drawTextImg('Turn: {:<12}'.format(turns+1), init.listImage['GUI']['Turn Phase'], 45, offsetHeight + 300, 320, 100, font=init.font30)
    WIN.blit(init.listImage['GUI']['Turn Phase Ef'], (45, offsetHeight + 300))
    try:
        WIN.blit(init.listImage['GEI']['Phase ' + str(phase)], (275, offsetHeight + 325))
    except:
        pass

    for i in range(len(init.HistoryLog)):
        card.drawText(WIN, init.HistoryLog[i], 'black', ((100, offsetHeight + 450 + i*40), (300, 100)), init.font20)

def update_display(win, nboard, pos, turns, phase):
    """
    Cập nhập cửa sổ hiển thị
    :param win: Cửa sổ hiển thị (pygame.image)
    :param nboard: Bàn cờ (board.Board)
    :param pos: Vị trí con trỏ chuột (tuple(int, int))
    :param turns: Lượt hiện tại (int)
    :param phase: Giai đoạn của lượt hiện tại (int)
    :return: None
    """
    WIN.fill('white')
    nboard.draw(win)
    ncard.draw(win, init.font40, pos, Players[turns % 2])
    if phase == chess.PHASE['Finish']:
        print('WIN')
        endGame()
    updateGUI()
    pygame.display.update()

def main():
    """
    Chạy game
    :return: None
    """
    turn_on_music()
    global pause, phase, turns, startTurnTime, timing, playingTeam, click
    redraw = False
    pause = False
    selected = False
    required = 0
    selectedPos = []
    playingTeam = 'w'
    while True:
        if phase == chess.PHASE['Start']:
            selected = False
            required = 0
            selectedPos = []
        if turns % 2 == 0:
            playingTeam = 'w'
        else:
            playingTeam = 'b'

        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == MUSIC_END:
                pygame.mixer.music.queue(init.listMusic[0])
                init.listMusic.append(init.listMusic.pop(0))

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
                    nboard.controlledCells(phase, playingTeam)
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
                            nboard.controlledCells(phase, playingTeam)
                            selected, moves = nboard.select_Chess(index, phase, playingTeam)
                            print(moves)
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
                            nboard.controlledCells(phase, playingTeam)
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
                        nboard.controlledCells(phase, playingTeam)
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
                        nboard.controlledCells(phase, playingTeam)
                        Players[turns % 2].decelect()
                        phase = Players[turns % 2].update((chess.PHASE['End']), init.DECK, False, startTurnTime)
                        selected = False
                        selectedPos = []
                        #-----------------------------------------------------------------------------------------------
                print("Phase:", phase)
                print("Turn:", turns)
                nboard.printMap()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused()
            check_evolutions()
        phase = Players[turns % 2].update(phase, init.DECK, init.SETTINGS['AddTimeable'], startTurnTime)
        if phase == chess.PHASE['End']:
            startTurnTime = math.floor(time.time())
        phase, turns = nboard.update(phase, turns, playingTeam)
        update_display(WIN, nboard, pygame.mouse.get_pos(), turns, phase)

def drawTextImg(text, img, x, y, width, height, color = 'black', font = init.font40, **param):
    """
    In các hình ảnh có chữ phía trên
    :param text: Văn bản hiển thị trên nút (str)
    :param img: Hình ảnh của nút (pygame.image)
    :param x: Tọa độ x của nút (int)
    :param y: Tọa độ y của nút (int)
    :param width: Chiều rộng của nút (int)
    :param height: Chiều cao của nút (int)
    :param color: Màu sắc của chữ được hiển thị (str|(int, int, int))
    :param font: Font chữ của chữ được hiển thị (font.Font)
    :param param: Các giá trị tùy chọn
    :return: None
    """
    img = pygame.transform.scale(img, (width, height))
    WIN.blit(img, (x, y))
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    WIN.blit(textSurface, textRect)

def button(text, img, img_h, x, y, width, height, action = None, color = 'black', font = init.font40, **param):
    """
    Tạo các nút trên màn hình
    :param text: Văn bản hiển thị trên nút (str)
    :param img: Hình ảnh của nút (pygame.image)
    :param img_h: Hình ảnh của nút khi con trỏ chuột đi qua (pygame.image)
    :param x: Tọa độ x của nút (int)
    :param y: Tọa độ y của nút (int)
    :param width: Chiều rộng của nút (int)
    :param height: Chiều cao của nút (int)
    :param action: Hàm được gọi khi nút được nhấn (str)
    :param color: Màu sắc của chữ được hiển thị (str|(int, int, int))
    :param font: Font chữ của chữ được hiển thị (font.Font)
    :param param: Các giá trị tùy chọn
    :return: None
    """

    img = pygame.transform.scale(img, (width, height))
    WIN.blit(img, (x, y))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        try:
            img_h = pygame.transform.scale(img_h, (width, height))
            WIN.blit(img_h, (x, y))
        except:
            pass
        if click[0] == 1 and action != None:
            print(mouse)
            if param != {}:
                action(param)
            else:
                action()
    if text != '':
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect()
        textRect.center = ((x + (width / 2)), (y + (height / 2)))
        WIN.blit(textSurface, textRect)

def paused():
    """
    Tạm dừng trận đấu
    :return: None
    """
    global timing, startTurnTime
    nowTime = math.floor(time.time())
    timing = nowTime - startTurnTime
    pygame.mixer.music.pause()
    global pause
    pause = True
    textSurface = init.font60.render('TẠM DỪNG', True, 'white')
    textRect = textSurface.get_rect()
    interval = (WinHeight - offsetHeight) / 6
    textRect.center = ((WinWidth / 2), offsetHeight*2)
    while pause:
        startTurnTime = math.floor(time.time()) - timing
        cell.Cell(0, 0, init.listImage[env]['Background']).draw(WIN, WinHeight, WinWidth)
        WIN.blit(pygame.transform.scale(init.listImage['GEI']['Darker'], (WIDTH, WinHeight)), (offsetWidth, 0))
        WIN.blit(textSurface, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main()
        button('CHƠI TIẾP', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363 / 2, 2 * interval, 363, 100, main)
        button('CHƠI MỚI', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363 / 2, 3 * interval, 363, 100, setting_game)
        button('MENU', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363 / 2, 4 * interval, 363, 100, game_intro)
        button('THOÁT', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363 / 2, 5 * interval, 363, 100, end_game)
        pygame.display.update()

def endGame():
    """
    Kết thúc trận đấu
    :return: None
    """
    pygame.mixer.music.pause()
    global pause
    pause = True
    textSurface = init.font60.render('Player ' + str(turns % 2 + 1) + ' WIN', True, 'white')
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
        button('CHƠI LẠI', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363 / 2, 2 * interval, 363, 100, new_game)
        button('MENU', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363 / 2, 3 * interval, 363, 100, game_intro)
        button('THOÁT', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363 / 2, 4 * interval, 363, 100, end_game)
        pygame.display.update()

def end_turn():
    """
    Kết thúc lượt
    :return: None
    """
    global phase, nboard, turns
    Players[turns % 2].decelect()
    nboard.deselect()
    nboard.controlledCells(phase, playingTeam)
    phase = chess.PHASE['End']

def end_game():
    """
    Thoát game
    :return: None
    """
    pygame.quit()
    quit()

def check_evolutions():
    """
    Kiểm tra thăng cấp cho quân "Chốt"
    :return: None
    """
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
                if object[1].get_type() == 'Pawn' and object[0][1] == 7*(object[1].get_direction()>0):
                    WIN.blit(pygame.transform.scale(init.listImage['GEI']['Darker'], (WinWidth, WinHeight)), (0, 0))
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                end_game()
                        button('', init.listImage['Chess Art']['Queen'], init.listImage['GEI']['Darken'], WinWidth / 2 - 315, WinHeight / 2 - 200, 150, 322, evolution, type='Queen', team = object[1].get_team(), oBoard = oBoard, index = object[0])
                        button('', init.listImage['Chess Art']['Bishop'], init.listImage['GEI']['Darken'], WinWidth / 2 - 155, WinHeight / 2 - 122, 150, 322, evolution, type='Bishop', team = object[1].get_team(), oBoard = oBoard, index = object[0])
                        button('', init.listImage['Chess Art']['Knight'], init.listImage['GEI']['Darken'], WinWidth / 2 + 5, WinHeight / 2 - 200, 150, 322, evolution, type='Knight', team = object[1].get_team(), oBoard = oBoard, index = object[0])
                        button('', init.listImage['Chess Art']['Rook'], init.listImage['GEI']['Darken'], WinWidth / 2 + 165, WinHeight / 2 - 122, 150, 322, evolution, type='Rook', team = object[1].get_team(), oBoard = oBoard, index = object[0])
                        pygame.display.update()
            except:
                pass

def game_intro():
    """
    Màn hình chờ của game
    :return: None
    """
    global pause
    pause = True
    pygame.time.delay(50)
    textSurface = init.font60.render('CHESS: MAGIC CARD', True, 'white')
    textRect = textSurface.get_rect()
    interval = (WinHeight - offsetHeight) / 6
    textRect.center = ((WinWidth / 2), offsetHeight*2)
    while pause:
        cell.Cell(0, 0, init.listImage['Random']['Intro']).draw(WIN, WinHeight, WinWidth)
        WIN.blit(textSurface, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game()
        button('BẮT ĐẦU', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363 / 2, 2.5 * interval, 363, 100, setting_game)
        button('THOÁT', init.listImage['GUI']['Button'], init.listImage['GUI']['Hover_Button'], (WinWidth / 2) - 363 / 2, 3.5 * interval, 363, 100, end_game)
        pygame.display.update()