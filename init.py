import pygame
import environment as env
import effect as ef
from card import Card
import chess
import random

listImage = {
    'b': {
        'b':pygame.image.load('img\\b_bishop.png'), 'k':pygame.image.load('img\\b_king.png'),
        'kn':pygame.image.load('img\\b_knight.png'), 'p':pygame.image.load('img\\b_pawn.png'),
        'q':pygame.image.load('img\\b_queen.png'), 'r':pygame.image.load('img\\b_rook.png')
    },
    'w': {
        'b':pygame.image.load('img\\w_bishop.png'), 'k':pygame.image.load('img\\w_king.png'),
        'kn':pygame.image.load('img\\w_knight.png'), 'p':pygame.image.load('img\\w_pawn.png'),
        'q':pygame.image.load('img\\w_queen.png'), 'r':pygame.image.load('img\\w_rook.png')
    },
    'GEI': {
        'Normal':pygame.image.load('img\\GEI\\classic_normal.png'),
        'Darken':pygame.image.load('img\\GEI\\darkcell.png'),
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
    },
    'Cards': {
        '01':pygame.image.load('img\\Card\\01.png'),
        '02':pygame.image.load('img\\Card\\02.png'),
        '03':pygame.image.load('img\\Card\\03.png'),
        '04':pygame.image.load('img\\Card\\04.png'),
        '05':pygame.image.load('img\\Card\\05.png'),
        '06':pygame.image.load('img\\Card\\06.png')
    },
    'Desert': {
        'Normal':pygame.image.load('img\\Environment\\desert_normal.png'),
        'Special':pygame.image.load('img\\Environment\\derest_special.png')
    },
    'Frozen_river':{
        'Normal':pygame.image.load('img\\Environment\\frozen_river_normal.png'),
        'Special':pygame.image.load('img\\Environment\\frozen_river_special.png'),
        'Triggered_effect':pygame.image.load('img\\Environment\\frozen_river_hole.png')
    },
    'Foggy_forest': {
        'Normal':pygame.image.load('img\\Environment\\foggy_forest_normal.png'),
        'Special':pygame.image.load('img\\Environment\\foggy_forest_special.png')
    },
    'Swamp': {
        'Normal':pygame.image.load('img\\Environment\\swamp_normal.png'),
        'Special':pygame.image.load('img\\Environment\\swamp_special.png')
    },
    'Grassland': {
        'Normal':pygame.image.load('img\\Environment\\grassland.png')
    }
}

pygame.font.init()
font20 = pygame.font.Font('font\\Comfortaa-VariableFont_wght.ttf', 20)
font40 = pygame.font.Font('font\\static\\Comfortaa-SemiBold.ttf', 40)
font60 = pygame.font.Font('font\\static\\Comfortaa-SemiBold.ttf', 60)

EFFECT = {

}

DECK = [
    Card('Tiến Công', 2, listImage['Cards']['01'], 'Tiến thẳng hoặc chéo về phía trước 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Ahead Left', 'Ahead', 'Ahead Right'], killable = False),
    Card('Rút Lui', 2, listImage['Cards']['02'], 'Lùi hoặc chéo về phía sau 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Back Left', 'Back', 'Back Right'], killable = False),
    Card('Tấn Công Mạn Sườn', 2, listImage['Cards']['03'], 'Đi ngang sang trái hoặc phải 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Left', 'Right'], killable = False),
    Card('Đánh Phủ Đầu', 3, listImage['Cards']['04'], 'Tấn công về phía trước 2 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 2)], directions = ['Ahead'], killable = True),
    Card('Đánh Phủ Đầu', 3, listImage['Cards']['05'], 'Tấn công về phía trước 2 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions=['Back'], killable = True),
    Card('Linh Động Chiến Trường', 3, listImage['Cards']['06'], 'Di chuyển về 1 hướng bất kỳ 2 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns=1, phase=3, value=1)], directions=['Ahead Left', 'Ahead', 'Ahead Right', 'Back Left', 'Back', 'Back Right', 'Left', 'Right'], killable=False)
]

ENVIRONMENT = {
    'Desert':env.Desert(listImage['Desert'], 800),
    'Frozen_river':env.Frozen_river(listImage['Frozen_river'], 800),
    'Foggy_forest':env.Foggy_forest(listImage['Foggy_forest'], 800),
    'Swamp':env.Swamp(listImage['Swamp'], 800),
    'Grassland':env.Grassland(listImage['Grassland'], 800)
}