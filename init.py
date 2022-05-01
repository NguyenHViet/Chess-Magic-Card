import pygame
import effect
from card import Card

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
        'Normal':pygame.image.load('img\\classic_normal.png'),
        'Darken':pygame.image.load('img\\darkcell.png'),
        'Move':pygame.image.load('img\\move.png'),
        'Choice':pygame.image.load('img\\choice.png')
    }
}

pygame.font.init()
font = pygame.font.Font('font\\Comfortaa-VariableFont_wght.ttf', 20)

EFFECT = {

}

DECK = [
    Card('Tiến Công', 1, listImage['b']['p'], 'Tiến về phía trước hoặc chéo tới 1 ô', 'GoAhead', 2),
    Card('Rút Lui', 1, listImage['b']['k'], 'Lùi về phía sau hoặc chéo lui 1 ô', 'GoBack', 2),
    Card('Đảo Chiều', 1, listImage['b']['r'], 'Đi ngang sang trái hoặc phải 1 ô', 'GoHorizontal', 2)
]