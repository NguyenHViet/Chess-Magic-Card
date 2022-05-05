import pygame
import enviroment as env
import effect as ef
from card import Card
import chess

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
        'Card_Cell':pygame.image.load('img\\GEI\\card_area.png')
    },
    'GUI': {
        'EndTurn': pygame.image.load('img\\GUI\\end_turn_button.png'),
        'Choice':pygame.image.load('img\\GUI\\choice_white.png'),
        'Pause':pygame.image.load('img\\GUI\\pause_button.png'),
        'Button':pygame.image.load('img\\GUI\\button.png'),
        'Hover_Button':pygame.image.load('img\\GUI\\button_hover.png')
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
        'Normal':pygame.image.load('img\\Desert\\desert_normal.jpg')
    }
}

""" 'Desert_Normal':pygame.image.load(enviroment.Desert.get_env_img()['normal']),
'Frozen_river_Normal':pygame.image.load(enviroment.Frozen_river.get_env_img()['normal']),
'Foggy_forest_Normal':pygame.image.load(enviroment.Foggy_forest.get_env_img()['normal']),
'Swamp_Normal':pygame.image.load(enviroment.Swamp.get_env_img()['normal']),
'Grassland':pygame.image.load(enviroment.Grassland.get_env_img()['normal']),
'Desert_Speacial':pygame.image.load(enviroment.Desert.get_env_img()['speacial']),
'Frozen_river_Speacial':pygame.image.load(enviroment.Frozen_river.get_env_img()['speacial']),
'Foggy_forest_Speacial':pygame.image.load(enviroment.Foggy_forest.get_env_img()['speacial']),
'Swamp_Speacial':pygame.image.load(enviroment.Swamp.get_env_img()['speacial']),"""

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
    Card('Linh Động Chiến Trường', 3, listImage['Cards']['06'], 'Di chuyển về 1 hướng bất kỳ 2 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns=1, phase=3, value=2)], directions=['Ahead Left', 'Ahead', 'Ahead Right', 'Back Left', 'Back', 'Back Right', 'Left', 'Right'], killable=False)
]

ENVIRONMENT = {
    'Desert':env.Simp(listImage['GEI'])
}