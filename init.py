import pygame
import environment as env
import effect as ef
from card import Card
import chess
import random

listImage = {
    'b': {
        'Bishop':pygame.image.load('img\\Chess\\b_bishop.png'), 'King':pygame.image.load('img\\Chess\\b_king.png'),
        'Knight':pygame.image.load('img\\Chess\\b_knight.png'), 'Pawn':pygame.image.load('img\\Chess\\b_pawn.png'),
        'Queen':pygame.image.load('img\\Chess\\b_queen.png'), 'Rook':pygame.image.load('img\\Chess\\b_rook.png')
    },
    'w': {
        'Bishop':pygame.image.load('img\\Chess\\w_bishop.png'), 'King':pygame.image.load('img\\Chess\\w_king.png'),
        'Knight':pygame.image.load('img\\Chess\\w_knight.png'), 'Pawn':pygame.image.load('img\\Chess\\w_pawn.png'),
        'Queen':pygame.image.load('img\\Chess\\w_queen.png'), 'Rook':pygame.image.load('img\\Chess\\w_rook.png')
    },
    'Chess Art':{
        'Queen':pygame.image.load('img\\Chess\\m_queen.png'),
        'Rook': pygame.image.load('img\\Chess\\m_rook.png'),
        'Knight': pygame.image.load('img\\Chess\\m_knight.png'),
        'Bishop': pygame.image.load('img\\Chess\\m_bishop.png'),
    },
    'GEI': {
        'Normal':pygame.image.load('img\\GEI\\classic_normal.png'),
        'Darken':pygame.image.load('img\\GEI\\darkcell.png'),
        'Darker':pygame.image.load('img\\GEI\\darker.png'),
        'Move':pygame.image.load('img\\GEI\\move.png'),
        'Choice':pygame.image.load('img\\GEI\\choice.png'),
        'Hover':pygame.image.load('img\\GEI\\choice_magic.png'),
        'Card_Hover':pygame.image.load('img\\GEI\\card_hover.png'),
        'Card_Picking':pygame.image.load('img\\GEI\\picking_card.png'),
        'Card_Cell':pygame.image.load('img\\GEI\\card_area.png'),
        'LockCard': pygame.image.load('img\\GEI\\lock_card.png'),
        'Empty':pygame.image.load('img\\GEI\\empty.png')
    },
    'GUI': {
        'EndTurn': pygame.image.load('img\\GUI\\end_turn_button.png'),
        'Choice':pygame.image.load('img\\GUI\\choice_white.png'),
        'Pause':pygame.image.load('img\\GUI\\pause_button.png'),
        'Button':pygame.image.load('img\\GUI\\button.png'),
        'Hover_Button':pygame.image.load('img\\GUI\\button_hover.png'),
        'Black Timer':pygame.image.load('img\\GUI\\b_timer.png'),
        'White Timer':pygame.image.load('img\\GUI\\w_timer.png'),
        'Actions': pygame.image.load('img\\GUI\\actions.png'),
        'Lock':pygame.image.load('img\\GUI\\lock.png'),
        'Arrow_Up':pygame.image.load('img\\GUI\\arrow_up.png'),
        'Arrow_Down': pygame.image.load('img\\GUI\\arrow_down.png'),
        'Arrow_Left': pygame.image.load('img\\GUI\\arrow_left.png'),
        'Arrow_Right': pygame.image.load('img\\GUI\\arrow_right.png'),
        'Turn Phase':pygame.image.load('img\\GUI\\turn_phase_bot.png'),
        'Turn Phase Ef': pygame.image.load('img\\GUI\\turn_phase.png'),
        'Random':pygame.image.load('img\\GUI\\random_button.png'),
        'Mute':pygame.image.load('img\\GUI\\mute_button.png'),
        'Unmute': pygame.image.load('img\\GUI\\unmute_button.png'),
        'Env Timer':pygame.image.load('img\\GUI\\evironment_timer.png'),
        'Env Timer Ef': pygame.image.load('img\\GUI\\evironment_timer_ef.png'),
    },
    'Cards': {
        '01':pygame.image.load('img\\Card\\01.png'),
        '02':pygame.image.load('img\\Card\\02.png'),
        '03':pygame.image.load('img\\Card\\03.png'),
        '04':pygame.image.load('img\\Card\\04.png'),
        '05':pygame.image.load('img\\Card\\05.png'),
        '06':pygame.image.load('img\\Card\\06.png'),
        '07':pygame.image.load('img\\Card\\07.png')
    },
    'Desert': {
        'Normal':pygame.image.load('img\\Environment\\desert_normal.png'),
        'Special':pygame.image.load('img\\Environment\\derest_special.png'),
        'Background':pygame.image.load('img\\Environment\\desert_bg.jpg'),
        'Prepare':pygame.image.load('img\\Environment\\derest_prepare.png')
    },
    'Frozen River':{
        'Normal':pygame.image.load('img\\Environment\\frozen_river_normal.png'),
        'Special':pygame.image.load('img\\Environment\\frozen_river_special.png'),
        'Special 2':pygame.image.load('img\\Environment\\frozen_river_special_2.png'),
        'Triggered_effect':pygame.image.load('img\\Environment\\frozen_river_hole.png'),
        'Background': pygame.image.load('img\\Environment\\desert_bg.jpg')
    },
    'Foggy Forest': {
        'Normal':pygame.image.load('img\\Environment\\foggy_forest_normal.png'),
        'Special':pygame.image.load('img\\Environment\\foggy_forest_special.png'),
        'Background': pygame.image.load('img\\Environment\\foggy_forest_bg.jpg')

    },
    'Swamp': {
        'Normal':pygame.image.load('img\\Environment\\swamp_normal.png'),
        'Special':pygame.image.load('img\\Environment\\swamp_special.png'),
        'Background': pygame.image.load('img\\Environment\\swamp_bg.jpg')
    },
    'Grassland': {
        'Normal':pygame.image.load('img\\Environment\\grassland.png'),
        'Background': pygame.image.load('img\\Environment\\desert_bg.jpg')
    },
    'Random': {
        'Background':pygame.image.load('img\\Environment\\random_bg.jpg')
    }
}

pygame.font.init()
font15 = pygame.font.Font('font\\Comfortaa-VariableFont_wght.ttf', 15)
font20 = pygame.font.Font('font\\Comfortaa-VariableFont_wght.ttf', 20)
font25 = pygame.font.Font('font\\Comfortaa-VariableFont_wght.ttf', 25)
font30 = pygame.font.Font('font\\Comfortaa-VariableFont_wght.ttf', 30)
font40 = pygame.font.Font('font\\static\\Comfortaa-SemiBold.ttf', 40)
font50 = pygame.font.Font('font\\static\\Comfortaa-SemiBold.ttf', 50)
font60 = pygame.font.Font('font\\static\\Comfortaa-SemiBold.ttf', 60)

EFFECT = {

}

DECK = [
    Card('Tiến Công', 2, listImage['Cards']['01'], 'Tiến thẳng về phía trước 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Ahead Left', 'Ahead', 'Ahead Right'], killable = False),
    Card('Rút Lui', 2, listImage['Cards']['02'], 'Lùi về phía sau 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Back Left', 'Back', 'Back Right'], killable = False),
    Card('Tấn Công Mạn Sườn', 2, listImage['Cards']['03'], 'Đi ngang sang trái hoặc phải 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Left', 'Right'], killable = False),
    Card('Đánh Phủ Đầu', 3, listImage['Cards']['04'], 'Tấn công về phía trước 2 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 2)], directions = ['Ahead'], killable = True),
    Card('Đánh Phủ Đầu', 3, listImage['Cards']['05'], 'Tấn công về phía trước 2 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions=['Back'], killable = True),
    Card('Linh Động Chiến Trường', 3, listImage['Cards']['06'], 'Di chuyển về 1 hướng bất kỳ 2 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns=1, phase=3, value=1)], directions=['Ahead Left', 'Ahead', 'Ahead Right', 'Back Left', 'Back', 'Back Right', 'Left', 'Right'], killable=False),
    Card('Tấm Khiên Cứng Cáp', 3, listImage['Cards']['07'], 'Không thể bị chọn trong 3 lượt', 'GrantEffects', 1, [ef.Effect('Unselectable', turns = 3, phase=[2, 3])]),

]

ENVIRONMENT = {
    'Desert':env.Desert(listImage['Desert'], 800),
    'Frozen River':env.Frozen_river(listImage['Frozen River'], 800),
    'Foggy Forest':env.Foggy_forest(listImage['Foggy Forest'], 800),
    'Swamp':env.Swamp(listImage['Swamp'], 800),
    'Grassland':env.Grassland(listImage['Grassland'], 800),
    'Random':env.Environment(),
}