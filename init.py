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
font = pygame.font.Font('font\\Comfortaa-VariableFont_wght.ttf', 20)

EFFECT = {

}

DECK = [
    Card('Tiến Công', 2, listImage['b']['p'], 'Tiến về phía trước hoặc chéo tới 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Ahead Left', 'Ahead', 'Ahead Right'], killable = False),
    Card('Rút Lui', 2, listImage['b']['k'], 'Lùi về phía sau hoặc chéo lui 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Back Left', 'Back', 'Back Right'], killable = False),
    Card('Đảo Chiều', 1, listImage['b']['r'], 'Đi ngang sang trái hoặc phải 1 ô', 'ActiveEffects', 2, [ef.Effect('PushChess', turns = 1, phase = 3, value = 1)], directions = ['Left', 'Right'], killable = False),

]

ENVIRONMENT = {
    'Desert':env.Simp(listImage['GEI'])
}